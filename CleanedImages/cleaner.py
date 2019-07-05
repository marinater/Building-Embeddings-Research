from PIL import Image
import cv2
import numpy as np
import os
import cv2
from scipy import ndimage

kernels = [
	('fourway', np.array([[0,0,1,0,0],[0,0,1,0,0],[1,1,1,1,1],[0,0,1,0,0],[0,0,1,0,0]], dtype='uint8')),
	('north_threeway', np.array([[0,0,1,0,0],[0,0,1,0,0],[0,0,1,0,0],[0,0,1,0,0],[1,1,1,1,1]], dtype='uint8')),
	('south_threeway', np.array([[1,1,1,1,1],[0,0,1,0,0],[0,0,1,0,0],[0,0,1,0,0],[0,0,1,0,0]], dtype='uint8')),
	('east_threeway', np.array([[1,0,0,0,0],[1,0,0,0,0],[1,1,1,1,1],[1,0,0,0,0],[1,0,0,0,0]], dtype='uint8')),
	('west_threeway', np.array([[0,0,0,0,1],[0,0,0,0,1],[1,1,1,1,1],[0,0,0,0,1],[0,0,0,0,1]], dtype='uint8')),
	('b_l_corner', np.array([[1,0,0,0,0],[1,0,0,0,0],[1,0,0,0,0],[1,0,0,0,0],[1,1,1,1,1]], dtype='uint8')),
	('b_r_corner', np.array([[0,0,0,0,1],[0,0,0,0,1],[0,0,0,0,1],[0,0,0,0,1],[1,1,1,1,1]], dtype='uint8')),
	('t_l_corner', np.array([[1,1,1,1,1],[1,0,0,0,0],[1,0,0,0,0],[1,0,0,0,0],[1,0,0,0,0]], dtype='uint8')),
	('t_r_corner', np.array([[1,1,1,1,1],[0,0,0,0,1],[0,0,0,0,1],[0,0,0,0,1],[0,0,0,0,1]], dtype='uint8')),
	('v_line', np.array([[0,0,1,0,0],[0,0,1,0,0],[0,0,1,0,0],[0,0,1,0,0],[0,0,1,0,0]], dtype='uint8')),
	('h_line', np.array([[0,0,0,0,0],[0,0,0,0,0],[1,1,1,1,1],[0,0,0,0,0],[0,0,0,0,0]], dtype='uint8')),
	('dot', np.array([[0,0,0,0,0],[0,1,1,1,0],[0,1,1,1,0],[0,1,1,1,0],[0,0,0,0,0]], dtype='uint8'))
]

kernelsDict = {
	'fourway' : np.array([[0,0,255,0,0],[0,0,255,0,0],[255,255,255,255,255],[0,0,255,0,0],[0,0,255,0,0]], dtype='uint8'),
	'north_threeway' : np.array([[0,0,255,0,0],[0,0,255,0,0],[0,0,255,0,0],[0,0,255,0,0],[255,255,255,255,255]], dtype='uint8'),
	'south_threeway' : np.array([[255,255,255,255,255],[0,0,255,0,0],[0,0,255,0,0],[0,0,255,0,0],[0,0,255,0,0]], dtype='uint8'),
	'east_threeway' : np.array([[255,0,0,0,0],[255,0,0,0,0],[255,255,255,255,255],[255,0,0,0,0],[255,0,0,0,0]], dtype='uint8'),
	'west_threeway' : np.array([[0,0,0,0,255],[0,0,0,0,255],[255,255,255,255,255],[0,0,0,0,255],[0,0,0,0,255]], dtype='uint8'),
	'b_l_corner' : np.array([[255,0,0,0,0],[255,0,0,0,0],[255,0,0,0,0],[255,0,0,0,0],[255,255,255,255,255]], dtype='uint8'),
	'b_r_corner' : np.array([[0,0,0,0,255],[0,0,0,0,255],[0,0,0,0,255],[0,0,0,0,255],[255,255,255,255,255]], dtype='uint8'),
	't_l_corner' : np.array([[255,255,255,255,255],[255,0,0,0,0],[255,0,0,0,0],[255,0,0,0,0],[255,0,0,0,0]], dtype='uint8'),
	't_r_corner' : np.array([[255,255,255,255,255],[0,0,0,0,255],[0,0,0,0,255],[0,0,0,0,255],[0,0,0,0,255]], dtype='uint8'),
	'v_line' : np.array([[0,0,255,0,0],[0,0,255,0,0],[0,0,255,0,0],[0,0,255,0,0],[0,0,255,0,0]], dtype='uint8'),
	'h_line' : np.array([[0,0,0,0,0],[0,0,0,0,0],[255,255,255,255,255],[0,0,0,0,0],[0,0,0,0,0]], dtype='uint8'),
	'dot' : np.array([[0,0,0,0,0],[0,255,255,255,0],[0,255,255,255,0],[0,255,255,255,0],[0,0,0,0,0]], dtype='uint8'),
	'' : np.zeros((5,5), dtype='uint8'),
	'empty' : np.zeros((5,5), dtype='uint8'),
}

def identify_tile(img):
	ret, img2 = cv2.threshold(img, 100, 255, cv2.THRESH_BINARY)
	img2 = cv2.copyMakeBorder(img2, 5, 5, 5, 5, cv2.BORDER_CONSTANT)

	if np.count_nonzero(img2) == 0: return 'empty'

	for tag, kernel in kernels:
		out = cv2.erode(img2, kernel, iterations = 1)
		out = out[5:-5, 5:-5]

		_, count = ndimage.label(out)
		if count > 0: return tag

	return ''

filenames = os.listdir('./cleaned')

width, height, chopsize = 256, 256, 16

for image_index, filename in enumerate(filenames[:400]):
	img = np.array(Image.open('./cleaned/' + filename))
	
	for x0 in range(0, 16):
		row = ''
		for y0 in range(0, 16):
			tag = identify_tile(img[x0*16: (x0*16) + chopsize, y0*16: (y0*16) + chopsize])
			row += tag + ' '
		print(row[:-1], end=';')