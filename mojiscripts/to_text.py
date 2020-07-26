# coding=utf-8
import json
import re
import sys
from io import open
from spellchecker import SpellChecker

from PIL import Image, ImageFont, ImageDraw

trans_file = "tracked/trashgomi/translation.trans"
out_file = "mojiscripts/translation.txt"

columns = ["Original Text", "Notes", "Character", "Initial", "Final"]

with open(trans_file, "rb") as f:
	j = json.load(f)
	output = ""
	for filename, data in list(j["project"]["files"].items()):
		for line, text in enumerate(data["data"]):
			for c in range(len(columns) - 1, 1, -1):
				if c + 1 > len(text):
					print("{}: line {} - text did not have enough columns!".format(filename, l + 1))
					exit(-1)
				en_text = text[c]
				if en_text:
					if bool(en_text.strip()):
						output += en_text.replace("\n", " ")
						output += "\n"

						break

with open(out_file, "w", encoding="UTF-8") as out:
	out.write(output)

print("Done!")