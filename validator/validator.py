# coding=utf-8
import re
import sys

from PIL import ImageFont
from io import open

import json

debug = False
trans_file = "tracked/trashgomi/translation.trans"
font_size = 22
font_path = "C:\\WINDOWS\\FONTS\\MSGOTHIC.TTC"  # Must be correctly set for your system!
font = ImageFont.truetype(font_path, font_size, 1)  # Face 1 = MS PGothic
cutoff_px = 444

skip_files = []

skip_indices = [
    ("Commonevents.txt", 18),
    ("Commonevents.txt", 19),
    ("Commonevents.txt", 20),
    ("Map039.txt", 0)
]

character_blacklist = [
    '…',  # Use three periods ...
    '~',  # Use a Japanese wave dash 〜
    'ー'  # Use an Em dash —
]

columns = [
    "Original Text",
    "Notes",
    "Character",
    "Initial",
    "Checked",
    "Localized",
    "Padding Column"
]

if debug:
    lines = [
        "I thought she was just a character in the story",
        "The meeting room is through here. You may enter,",
        "Palace guards must devote themselves to throwing",
        "The coffee served here is absolutely delicious ♪"
    ]
    for line in lines:
        w = font.getsize(line)[0]
        print("{}: {}".format(line, w))
else:
    with open(trans_file, "rb") as f:
        j = json.load(f)

    spec_file = None
    found_spec_file = False
    if len(sys.argv) > 1:
        spec_file = str(sys.argv[1])
        spec_file = spec_file.partition(".")[0]
        print("Only validating file matching name '{}'".format(spec_file))
    else:
        print("Validating all files in project")

    line_count = -1
    translated_count = 0
    problems = 0
    for filename, data in list(j["project"]["files"].items()):
        if filename in skip_files:
            continue
        print_break = False
        for l, text in enumerate(data["data"]):
            if (filename, l) in skip_indices:
                continue
            if spec_file:
                if filename.partition(".")[0] != spec_file:
                    continue
                elif not found_spec_file:
                    print("Found specified file!")
                    found_spec_file = True
            en_text = ""
            c = len(columns) - 1
            for c in range(len(columns) - 1, 2, -1):
                en_text = text[c]
                if en_text:
                    if bool(en_text.strip()):
                        break
                    else:
                        print("{}: line {}, column {} {} - whitespace only!".format(filename, l + 1, c + 1, columns[c]))
                        problems += 1
                        en_text = ""
                        print_break = True
            line_count += 1
            if type(en_text) != str:
                continue
            if not en_text:
                continue
            translated_count += 1
            for character in character_blacklist:
                if character in en_text:
                    print("{}: line {}, column {} {} - bad character ({})".format(
                        filename, l + 1, c + 1, columns[c], character))
                    problems += 1
                    print_break = True
            en_text = re.sub("\\\C\[\d\]", "", en_text)
            lines = en_text.split("\n")
            if len(lines) > 4:
                print("{}: line {}, column {} {} - too many lines ({}/4)".format(
                    filename, l + 1, c + 1, columns[c], len(lines)))
                problems += 1
                print_break = True

            bad_lines = []
            feedback = "{}: line {}, column {} {} - ".format(filename, l + 1, c + 1, columns[c])
            for i in range(0, len(lines)):
                w = font.getsize(lines[i])[0]
                if w > cutoff_px:
                    bad_lines.append(i)
                    problems += 1
                    feedback += "[too long] "
                if lines[i] != lines[i].lstrip():
                    bad_lines.append(i)
                    problems += 1
                    feedback += "[starts with whitespace] "
            if len(bad_lines) > 0:
                print_break = True
                print(feedback)
                for j in range(0, len(lines)):
                    w = font.getsize(lines[j])[0]
                    arrow = "<" if j in bad_lines else ""
                    print("{} ({}/{}px) {}".format(lines[j], w, cutoff_px, arrow))
                print()
        if print_break:
            print()
    if spec_file:
        if found_spec_file:
            print("Lines translated: {}/{} in specified file.".format(translated_count, line_count))
        if not found_spec_file:
            print("Did not find specified file.")
    else:
        print("Done! Problems: {}".format(problems))
        print("Lines translated: {}/{} = {}%.".format(
            translated_count,
            line_count,
            (float(translated_count)/float(line_count)) * 100))
        if problems > 0:
            exit(-1)