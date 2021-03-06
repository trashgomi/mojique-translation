# coding=utf-8
import json
import re
import sys
from io import open

from PIL import ImageFont

debug = False
trans_file = "tracked/trashgomi/translation.trans"
font_size = 22
font_path = "C:\\WINDOWS\\FONTS\\MSGOTHIC.TTC"  # Must be correctly set for your system!
font = ImageFont.truetype(font_path, font_size, 1)  # Face 1 = MS PGothic
cutoff_px = 444

skip_files = [
    "Scripts.txt",
    "GameINI.txt",
    "Actors.txt"
]

skip_indices = [
    ("Commonevents.txt", 18),
    ("Commonevents.txt", 19),
    ("Commonevents.txt", 20),
    ("Map039.txt", 0),
    ("Map083.txt", 3),
    ("Map289.txt", 5),
    ("Map289.txt", 6),
    ("Map617.txt", 29),
    ("Map384.txt", 171),
    ("Map488.txt", 2),
    ("Map548.txt", 38),
    ("Map581.txt", 10),
    ("Map581.txt", 11),
    ("Map581.txt", 16),
]

pmemories = range(3058, 3842)

character_blacklist = [
    '…',  # Use three periods ...
    '~',  # Use a Japanese wave dash 〜
    'ー',  # Use an Em dash —
    '#',  # Just don't
]

line_end_punctuation = [
    '.',
    '!',
    '?',
    '”',
    '*',
    ')',
    ']',
    '—',
    '♪',
    '/',
    '】',
    '☆',
    'ﾉ',
    ',',
    ':',
    ';',
    "\"",
    "』",
    "↑",
]

columns = [
    "Original Text",
    "Notes",
    "Character",
    "Translation",
]

duplicate_whitelist = {
    "I-I'll be done in just a minute!!",
    "Save?",
    "Incidentally, Hamuko.",
    "Zzz...",

    "There are picture books here, but there's no"
    "one who'll read 'em to me since you're not"
    "allowed to shout...",

    "Understood.",
    "*glare*",
    "Thank God～!!",
    "You have my thanks.",
    "Indeed.",
    "U-Umm...",
    "I see.",
    "......!",
    "Understood.",
    "Yeah.",
    "Mm.",
    "U-Umm...",
    "...!",
    "...",
    "...Eh?",
    "*fidget*...",
    "......",
    "Haaah... haaah...",
    "That's right.",
    "No way...",
    "Fine by me.",
    "Phew...",
    "...!!",
    "...?!",
    "Yep.",
    "*gulp*...",
    "*glug*... *glug*...",
    "What is it?",
    "...Ah.",
    "...Kh!",
    "Let's go.",
    "Found you.",
    "This is...",
    "Ah!",
    "Is that right?",
    "Now, then.",
    "I agree.",
    "Oh...?",
    "Haah... haah...!",
    "Hm?",
    "...Eh...?",
    "Yup!",
    "Don't board",
    "(...!!)",
    "(Hoh...)",
    "...?!?!",
    "(Doyaaah!!)",
    "...Ah...",
    "...Ah!",
    "I-Is that so...",
    "Haah... haah...",
    "......!!",
    "Thank you very much.",
    "Huh?",
    "Y-Yes...",
    "(......)",
    "Huuuh?",
    "*glug*...",
    "What do you mean?",
}
use_whitelist = True

hashes = set()

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

    line_count = 0
    translated_count = 0
    problems = 0
    for filename, data in list(j["project"]["files"].items()):
        if filename in skip_files:
            continue
        problem_in_file = False
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

            for c in range(len(columns) - 1, 1, -1):
                if c + 1 > len(text):
                    print("{}: line {} - text did not have enough columns!".format(filename, l + 1))
                    exit(-1)
                en_text = text[c]
                if en_text:
                    if bool(en_text.strip()):
                        if c <= 2:
                            print("{}: line {}, column {} {} - bad column used as translation!".format(filename,
                                                                                                       l + 1,
                                                                                                       c + 1,
                                                                                                       columns[c]))
                            problems += 1
                            en_text = ""
                            problem_in_file = True
                        break
                    else:
                        print("{}: line {}, column {} {} - whitespace only!".format(filename, l + 1, c + 1, columns[c]))
                        problems += 1
                        en_text = ""
                        problem_in_file = True
            if text[0]:
                line_count += 1
            if type(en_text) != str:
                continue
            if not en_text:
                continue
            translated_count += 1

            if use_whitelist and not duplicate_whitelist.__contains__(en_text):
                text_hash = en_text.__hash__()
                if hashes.__contains__(text_hash):
                    print("{}: line {} - duplicate text ({})".format(filename, l + 1, en_text))
                    problems += 1
                    problem_in_file = True
                else:
                    hashes.add(text_hash)

            if not text[2] or text[2] not in {"System", "Sign", "Corrupt", "Slang", "Robot"}:
                if en_text[len(en_text) - 1] not in line_end_punctuation:
                    print("{}: line {}, column {} {} - unexpected end character {}".format(
                        filename,
                        l + 1,
                        c + 1,
                        columns[c],
                        en_text[len(en_text) - 1]))
                    # Don't consider as a real problem
                    problem_in_file = True

            for character in character_blacklist:
                if character in en_text:
                    print("{}: line {}, column {} {} - bad character ({})".format(
                        filename, l + 1, c + 1, columns[c], character))
                    # Don't consider as a real problem
                    problem_in_file = True

            en_text = re.sub("\\\C\[\d\]", "", en_text)
            lines = en_text.split("\n")
            if len(lines) > 4:
                print("{}: line {}, column {} {} - too many lines ({}/4)".format(
                    filename, l + 1, c + 1, columns[c], len(lines)))
                problems += 1
                problem_in_file = True

            bad_lines = []
            feedback = "{}: line {}, column {} {} - ".format(filename, l + 1, c + 1, columns[c])
            for i in range(0, len(lines)):
                w = font.getsize(lines[i])[0]
                if w > cutoff_px:
                    bad_lines.append(i)
                    problems += 1
                    feedback += "[too long] "
                if not (filename == 'Commonevents.txt' and l in pmemories or filename == 'Map735.txt'):
                    if lines[i] != lines[i].lstrip():
                        bad_lines.append(i)
                        problems += 1
                        feedback += "[starts with whitespace] "
                if re.search("\\w【|】\\w", lines[i]):
                    bad_lines.append(i)
                    problems += 1
                    feedback += "[contains adjoined 【】"
            if len(bad_lines) > 0:
                problem_in_file = True
                print(feedback)
                for j in range(0, len(lines)):
                    w = font.getsize(lines[j])[0]
                    arrow = "<" if j in bad_lines else ""
                    print("{} ({}/{}px) {}".format(lines[j], w, cutoff_px, arrow))
                print()
        if problem_in_file:
            print("Found problems in file {}.".format(filename))
            print()
    print("Done! Problems: {}".format(problems))
    if spec_file:
        if found_spec_file:
            print("Lines translated: {}/{} in specified file.".format(translated_count, line_count))
        if not found_spec_file:
            print("Did not find specified file.")
    else:
        print("Lines translated: {}/{} = {}%.".format(
            translated_count,
            line_count,
            (float(translated_count)/float(line_count)) * 100))
    if problems > 0:
        exit(-1)
