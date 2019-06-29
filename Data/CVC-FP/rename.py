import os

dirname = "./samarth2/test/"

filenames = os.listdir(dirname)

for index, filename in enumerate(filenames):
	# print(filename, index)
	os.rename(dirname + filename, dirname + str(index) + ".jpg")