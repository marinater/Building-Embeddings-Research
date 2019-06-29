import os
import numpy as np
from PIL import Image

filenames = os.listdir("./out-svgs")

for filename in filenames:
	im = Image.open('./out-svgs/' + filename).convert('RGBA')
	data = np.array(im)
	red, green, blue, alpha = data.T
	white_areas = (red == 255) & (blue == 142) & (green == 70)
	data[..., :-1][white_areas.T] = (0, 0, 0)
	img2 = Image.fromarray(data).convert('RGB')
	img2.save('./out-svgs2/' + filename)