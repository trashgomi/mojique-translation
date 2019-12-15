# coding=utf-8
import json
import sys
from io import open

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

        print("Copying columns: {}".format(from_j["colHeaders"]))
        to_j["columns"] = from_j["columns"]
        to_j["colHeaders"] = from_j["colHeaders"]
        to_j["project"]["files"] = from_j["project"]["files"]

        with open(to_file, "w", encoding="UTF-8") as f:
            json.dump(to_j, f, ensure_ascii=False)
        print("Finished!")
