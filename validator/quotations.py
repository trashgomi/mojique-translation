# coding=utf-8
import json
import sys
from io import open

trans_file = "tracked/trashgomi/translation.trans"

skip_files = [
    "Scripts.txt",
]

skip_indices = [
    ("Commonevents.txt", 1953),
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


# Does not support replacing _
def replace_quotes(dialogue: str, old_sym: str, new_left: str, new_right: str, except_prefix: list = None):
    if not dialogue.__contains__(old_sym):
        return None
    else:
        if except_prefix:
            for prefix in except_prefix:
                dialogue = dialogue.replace(old_sym + prefix, "_" + prefix)
        no_of_quotes = dialogue.count(old_sym)
        if no_of_quotes % 2 != 0:
            return -1
        else:
            while no_of_quotes != 0:
                dialogue = dialogue.replace(old_sym, new_left, 1)
                dialogue = new_right.join(dialogue.rsplit(old_sym, 1))
                no_of_quotes = dialogue.count(old_sym)
            if except_prefix:
                for prefix in except_prefix:
                    dialogue = dialogue.replace("_" + prefix, old_sym + prefix)
            return dialogue


with open(trans_file, "r", encoding="UTF-8") as f:
    j = json.load(f)

spec_file = None
found_spec_file = False
if len(sys.argv) > 1:
    spec_file = str(sys.argv[1])
    spec_file = spec_file.partition(".")[0]
    print("Only transforming file matching name '{}'".format(spec_file))
else:
    print("Transforming all files in project")

file_index = -1
for filename, data in list(j["project"]["files"].items()):
    file_index += 1
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
                    en_text = ""
        if type(en_text) != str:
            continue
        if not en_text:
            continue

        result = replace_quotes(en_text, '\"', '“', '”')
        if result == -1:
            print("Found odd numbers of double quotes in file {}, line {}".format(filename, l + 1))
        elif result:
            en_text = result

        # result = replace_quotes(en_text, '\'', '‘', '’', ['s', 'll', 't', 've', 'd', 'm', 're'])
        # if result == -1:
        #     print("Found odd numbers of single quotes in file {}, line {}".format(filename, l + 1))
        # elif result:
        #     en_text = result

        j["project"]["files"][filename]["data"][l][c] = en_text

    if print_break:
        print()
with open(trans_file, "w", encoding="UTF-8") as f:
    json.dump(j, f, ensure_ascii=False)

if spec_file:
    if not found_spec_file:
        print("Did not find specified file.")
else:
    print("Done!")
