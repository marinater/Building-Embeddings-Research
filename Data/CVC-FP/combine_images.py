from PIL import Image
import os
import numpy as np

svgFiles = os.listdir("./out-svgs")

for filename in svgFiles:
	img1 = Image.open('./out-svgs/' + filename).convert('RGB')
	img2 = Image.open('./out-images/' + filename).convert('RGB')

	output = imgs_comb = np.hstack([np.asarray(img1), np.asarray(img2)])
	img3 = Image.fromarray(output)
	img3.save('./Combined/' + filename)

	img1.close()
	img2.close()
	img3.close()