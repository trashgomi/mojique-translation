# coding=utf-8
import json
import sys
from io import open

skip_files = {
    "Scripts.txt",
    "Actors.txt",
    "GameINI.txt",
    "Skills.txt",
    "System.txt",
    "Map318.txt",
    "Map320.txt",
    "Map330.txt",
    "Map452.txt",
    "Map639.txt",
    "Map640.txt",
}

if len(sys.argv) < 2:
    print("Error, from_file must be specified")
    exit(-1)
else:
    from_file = str(sys.argv[1])
    with open(from_file, "r", encoding="UTF-8") as f:
        from_j = json.load(f)

    if len(sys.argv) < 3:
        print("Error, to_file must be specified")
        exit(-1)
    else:
        to_file = str(sys.argv[2])

        with open(to_file, "r", encoding="UTF-8") as f:
            to_j = json.load(f)

        no_cols = len(to_j["colHeaders"])

        missing_lines = {}
        errors = False
        for filename in to_j["project"]["files"]:
            if filename in skip_files:
                continue
            if filename not in from_j["project"]["files"]:
                errors = True
                print("File '{}' did not exist in FROM project for target file '{}'!".format(filename, filename))
                continue
            val = to_j["project"]["files"][filename]
            data = val["data"]
            new_length = len(data)
            old_length = len(from_j["project"]["files"][filename]["data"])
            if old_length < new_length:
                errors = True
                print("File '{}' is smaller in FROM project than TO project!".format(filename))
                continue

            for i in range(0, new_length, 1):
                from_line = from_j["project"]["files"][filename]["data"][i]
                original_text = from_line[0]
                if to_j["project"]["files"][filename]["data"][i][0] != original_text:
                    errors = True
                    print("File '{}', line {}: FROM project had JP '{}'; TO project had JP '{}'!".format(
                        filename, i+1, original_text, to_j["project"]["files"][filename]["data"][i][0]))
                    break
                for j in range(1, no_cols, 1):
                    if from_line[j]:
                        to_j["project"]["files"][filename]["data"][i][j] = from_line[j]

        for filename in from_j["project"]["files"]:
            if filename not in to_j["project"]["files"]:
                print("File '{}' in FROM project does not exist in TO project!".format(filename))

        if not errors:
            with open(to_file, "w", encoding="UTF-8") as f:
                json.dump(to_j, f, ensure_ascii=False)
                print("Finished!")
        else:
            print("Did not copy.")
