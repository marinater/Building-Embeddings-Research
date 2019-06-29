from PIL import Image
import cv2
import numpy as np
import os

iMatrix = np.identity(10, np.uint8)
iMatrixInv = np.fliplr(iMatrix)

horizontal_kernal = np.ones((10,1), np.uint8)
vertical_kernal = np.fliplr(horizontal_kernal)

def cleanImage(img, filename):
	cv2.normalize(img, img, 0, 255, cv2.NORM_MINMAX)
	ret, img = cv2.threshold(img, 10, 255, cv2.THRESH_BINARY_INV)

	img_horizontal = cv2.erode(img, horizontal_kernal, iterations=1)
	img_vertical = cv2.erode(img, vertical_kernal, iterations=1)
	img_diag1 = cv2.erode(img, iMatrix, iterations=1)
	img_diag2 = cv2.erode(img, iMatrixInv, iterations=1)

	img = img_horizontal

	cv2.imwrite('./cleaned2/' + filename + '.png', img)

filenames = os.listdir("raw")

for filename in filenames:
	pil_img = Image.open('./raw/' + filename).convert('L')
	img = np.array(pil_img)
	cleanImage(img, filename.strip('.gif').strip('.png'))