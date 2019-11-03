from PIL import ImageFont
from io import open

import json

trans_file = "tracked/trashgomi/translation.trans"
font_size = 18
font_path = "C:\\WINDOWS\\FONTS\\MSGOTHIC.TTC"  # Must be correctly set for your system!
font = ImageFont.truetype(font_path, font_size)
cutoff_px = 442

skip_files = []

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

with open(trans_file, "rb") as f:
    j = json.load(f)

for filename, data in list(j["project"]["files"].items()):
    if filename in skip_files:
        continue
    print_break = False
    for l, text in enumerate(data["data"]):
        en_text = ""
        c = len(columns) - 1
        for c in range(len(columns) - 1, 2, -1):
            en_text = text[c]
            if en_text:
                if bool(en_text.strip()):
                    break
                else:
                    print("{}: line {}, column {} {} - whitespace only!".format(filename, l + 1, c + 1, columns[c]))
                    en_text = ""
                    print_break = True
        if type(en_text) != str:
            continue
        if not en_text:
            continue
        for character in character_blacklist:
            if character in en_text:
                print("{}: line {}, column {} {} - bad character ({})".format(
                    filename, l + 1, c + 1, columns[c], character))
                print_break = True
        lines = en_text.split("\n")
        if len(lines) > 4:
            print("{}: line {}, column {} {} - too many lines ({}/4)".format(
                filename, l + 1, c + 1, columns[c], len(lines)))
            print_break = True
        for line in lines:
            w, h = font.getsize(line)
            if w > cutoff_px:
                un_text = "{}: line {}, column {} {} - too long ({}/{}px): {}".format(
                    filename, l + 1, c + 1, columns[c], w, cutoff_px, line)
                print(un_text)
                print_break = True
            elif line != line.lstrip():
                print("{}: line {}, column {} {} - line starts with whitespace: {}".format(
                    filename, l + 1, c + 1, columns[c], line))
                print_break = True
    if print_break:
        print()
