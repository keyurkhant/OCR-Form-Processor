import cv2 as cv
import numpy as np
from pdf2image import convert_from_bytes

def getROI(img):
	
	img = cv.resize(img , (1443 , 1702))

	imgList = []

	#Provider Information Form 1
	imgCrop1 = img[60:600,0:720]
	imgList.append(imgCrop1)

	# Order Information Form 1
	imgCrop2 = img[60:600,720:1443] 
	imgList.append(imgCrop2)	

	# Patient Demographic 1 Form 1
	imgCrop3 = img[640:955,0:730]
	imgList.append(imgCrop3)

	# Patient Demographic 2 Form 1
	imgCrop4 = img[640:955,725:1443]
	imgList.append(imgCrop4)

	# Patient Ethinicity Form 1
	imgCrop5 = img[952:1120,0:1443]
	imgList.append(imgCrop5)

	# Patient Insurance Form 1
	imgCrop6 = img[1120:1490,0:1443]
	imgList.append(imgCrop6)

	# For lab use only Form 1
	imgCrop7 = img[1490:1700,0:1443]
	imgList.append(imgCrop7)

	# Form 2 (Only One Region)
	#imgCrop8 = img2[685:1800,90:1600]
	#imgList.append(imgCrop8)
	
	return imgList