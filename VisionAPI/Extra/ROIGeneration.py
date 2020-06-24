import cv2 as cv
import numpy as np
from pdf2image import convert_from_bytes

def getROI():
	
	img = cv.imread('/root/Keyur Khant/Study/Others/OCR Hackathon/VisionAPI/Untitled-3.jpg')
	
	img = img[69:2269,0:1654]

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
	#imgCrop8 = img2[685:1800,90:1600]
	#imgList.append(imgCrop8)
	
	for img in imgList:
		cv.imshow('Window', img)
		cv.waitKey(0)
		cv.destroyAllWindows()

getROI()