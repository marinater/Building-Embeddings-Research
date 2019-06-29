from PIL import Image
import cv2
import numpy as np
import os

filenames = os.listdir('./cleaned')

for image_index, filename in enumerate(filenames[:10]):
	img = Image.open('./cleaned/' + filename)
	width, height, chopsize = 256, 256, 16

	image_number = 0
	for x0 in range(0, width, chopsize):
	   for y0 in range(0, height, chopsize):
	      box = (x0, y0,
	             x0+chopsize if x0+chopsize <  width else  width - 1,
	             y0+chopsize if y0+chopsize < height else height - 1)

	      img.crop(box).save('./chopped/%s-%s.jpg' % (image_index, image_number))
	      image_number += 1