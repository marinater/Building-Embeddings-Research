from PIL import Image
import cv2
import numpy as np
import os

def cleanImage(img, filename):
	ret, img = cv2.threshold(img, 175, 255, cv2.THRESH_BINARY_INV)

	kernel = np.ones((2,2), np.uint8)

	img = cv2.erode(img, kernel, iterations = 1)
	# img = cv2.dilate(img,kernel, iterations = 1)

	erode_size = 10
	img1 = cv2.erode(img, np.ones( (erode_size, 1), np.uint8), iterations = 1)
	img2 = cv2.erode(img, np.ones( (1, erode_size), np.uint8), iterations = 1)
	img3 = cv2.erode(img, np.identity( erode_size, np.uint8), iterations = 1)
	img4 = cv2.erode(img, np.fliplr(np.identity( erode_size, np.uint8)), iterations = 1)
	img = img1 + img2 + img3 + img4
	# params = cv2.SimpleBlobDetector_Params()

	# params.filterByCircularity = False
	# params.filterByColor = False
	# params.filterByArea = True
	# params.filterByConvexity = False
	# params.filterByInertia = False
	# params.minArea = 100

	# detector = cv2.SimpleBlobDetector_create(params)
	# keypoints = detector.detect(img)

	# print(keypoints)
	# img = cv2.drawKeypoints(img, keypoints, np.array([]), (0, 0, 255), cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)



	# nb_components, output, stats, centroids = cv2.connectedComponentsWithStats(img, connectivity=8)
	# sizes = stats[1:, -1]; nb_components = nb_components - 1

	# min_size = 50

	# img = np.zeros((output.shape))
	# for i in range(0, nb_components):
	#     if sizes[i] >= min_size:
	#         img[output == i + 1] = 255



	cv2.imwrite('./cleaned/' + filename + '.png', img)

filenames = os.listdir("raw")

for filename in filenames:
	pil_img = Image.open('./raw/' + filename).convert('L')
	img = np.array(pil_img)
	cleanImage(img, filename.strip('.gif').strip('.png'))