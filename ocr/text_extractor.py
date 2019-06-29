from PIL import Image, ImageDraw, ImageFont
import pyocr
import pyocr.builders
import os
import re

tools = pyocr.get_available_tools()
tool = tools[0]
langs = tool.get_available_languages()
lang = langs[0]


filenames = os.listdir("./raw")
regex = re.compile('[^a-zA-Z0-9]')
font = ImageFont.truetype("open-sans.ttf", 20)

for filename in filenames[80:100]:
	img = Image.open('./raw/' + filename)
	new_w = 800; new_h = int(new_w * img.size[1] / img.size[0])
	img = img.resize( (new_w, new_h), Image.ANTIALIAS)

	word_boxes = tool.image_to_string(	
		img,
		lang="eng",
		builder=pyocr.builders.WordBoxBuilder()
	)

	d = ImageDraw.Draw(img)

	for word in word_boxes:
		text = regex.sub('', word.content)
		if text == '': continue

		d.rectangle(word.position, fill=(255,255,255) )
		d.text(word.position[0], text, fill=(255,0,0), font=font)

	img.save('./parsed/' + filename)