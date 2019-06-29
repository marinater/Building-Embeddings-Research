from PIL import Image
import cv2
import numpy as np
import os

iMatrix = np.identity(10, np.uint8)
iMatrixInv = np.fliplr(iMatrix)

kernel = np.ones((2,2), np.uint8)

def cleanImage(img, filename):
	cv2.normalize(img, img, 0, 255, cv2.NORM_MINMAX)
	
	ret, img = cv2.threshold(img, 10, 255, cv2.THRESH_BINARY_INV)

	img = cv2.erode(img, kernel, iterations=1)
	img = cv2.dilate(img, kernel, iterations=1)

	nb_components, output, stats, centroids = cv2.connectedComponentsWithStats(img, connectivity=8)
	sizes = stats[1:, -1]; nb_components = nb_components - 1

	min_size = 50

	img = np.zeros((output.shape))
	for i in range(0, nb_components):
	    if sizes[i] >= min_size:
	        img[output == i + 1] = 255


	cv2.imwrite('./cleaned/' + filename + '.png', img)

filenames = os.listdir("raw")

for filename in filenames:
	pil_img = Image.open('./raw/' + filename).convert('L')
	img = np.array(pil_img)
	cleanImage(img, filename.strip('.gif').strip('.png'))