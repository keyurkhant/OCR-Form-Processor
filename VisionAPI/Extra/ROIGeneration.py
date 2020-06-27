import cv2 as cv
import numpy as np
from pdf2image import convert_from_bytes

def getROI(pdf):
	images = convert_from_bytes(pdf)

	img = images[0]
	img = np.array(img)
	img2 = images[1]
	img2 = np.array(img2)
	imgList = []

	#Provider Information Form 1
	imgCrop1 = img[270:860,60:850]
	imgList.append(imgCrop1)

	# Order Information Form 1
	imgCrop2 = img[270:860,840:1650] 
	imgList.append(imgCrop2)	

	# Patient Demographic 1 Form 1
	imgCrop3 = img[910:1250,60:850]
	imgList.append(imgCrop3)

	# Patient Demographic 2 Form 1
	imgCrop4 = img[910:1250,840:1650]
	imgList.append(imgCrop4)

	# Patient Ethinicity Form 1
	imgCrop5 = img[1250:1430,60:1650]
	imgList.append(imgCrop5)

	# Patient Insurance Form 1
	imgCrop6 = img[1440:1820,60:1650]
	imgList.append(imgCrop6)

	# For lab use only Form 1
	imgCrop7 = img[2050:2150,1050:1650]
	imgList.append(imgCrop7)

	# Form 2 (Only One Region)
	imgCrop8 = img2[700:1795,125:1585]
	imgList.append(imgCrop8)

	# Form 2 (Only right Part)
	imgCrop9 = img2[700:1800,870:1570]
	imgList.append(imgCrop9)
	
	return imgList