# coding=utf-8
import json
import re
import sys
from io import open

from PIL import Image, ImageFont, ImageDraw

trans_file = "tracked/trashgomi/translation.trans"
font_size = 22
font_path = "C:\\WINDOWS\\FONTS\\MSGOTHIC.TTC"  # Must be correctly set for your system!
font = ImageFont.truetype(font_path, font_size, 1)  # Face 1 = MS PGothic
cutoff_px = 444

columns = ["Original Text", "Notes", "Character", "Initial", "Final"]

render_line = ("Map315.txt", 5)

with open(trans_file, "rb") as f:
	j = json.load(f)

	for filename, data in list(j["project"]["files"].items()):
		if filename == render_line[0]:
			print("Found specified file!")

			for l, text in enumerate(data["data"]):
				if l == render_line[1]:
					print("Found specified line!")

					for c in range(len(columns) - 1, 1, -1):
						if c + 1 > len(text):
							print("{}: line {} - text did not have enough columns!".format(filename, l + 1))
							exit(-1)
						en_text = text[c]
						if en_text:
							image = Image.new("RGBA", (600, 150), (255, 255, 255))
							draw = ImageDraw.Draw(image)

							draw.text((10, 0), en_text, (0, 0, 0), font=font)
							img_resized = image.resize((188, 45), Image.ANTIALIAS)
							image.save("mojiscripts/render_output.png")

							break
						else:
							print("")

print("Done!")
