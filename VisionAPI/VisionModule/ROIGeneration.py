import cv2 as cv
import numpy as np
from pdf2image import convert_from_bytes

def getROI(img):
	
	img = cv.resize(img , (1443 , 1702))

	imgList = []

	# HCO Name
	imgCrop1 = img[100:172,0:720]
	imgList.append(imgCrop1)

	# Provider Name
	imgCrop2 = img[160:235,0:720] 
	imgList.append(imgCrop2)	

	# NPI Number
	imgCrop3 = img[230:320,0:720]
	imgList.append(imgCrop3)

	# Provider Address 
	imgCrop4 = img[310:380,0:720]
	imgList.append(imgCrop4)

	# Provider City
	imgCrop5 = img[370:440,0:720]
	imgList.append(imgCrop5)

	# Provider Phone
	imgCrop6 = img[430:500,0:720]
	imgList.append(imgCrop6)

	# Provider Fax
	imgCrop7 = img[490:560,0:720]
	imgList.append(imgCrop7)




#################################

	# ICD 10 code
	imgCrop3 = img[210:360,720:1443]
	imgList.append(imgCrop3)

	# Date of order 
	imgCrop4 = img[500:600,1110:1443]
	imgList.append(imgCrop4)

#################################

	# Patient ID
	imgCrop5 = img[640:700,0:720]
	imgList.append(imgCrop5)

	# Patient first name
	imgCrop6 = img[695:750,0:315]
	imgList.append(imgCrop6)

	# Patient Last Name
	imgCrop7 = img[695:750,312:720]
	imgList.append(imgCrop7)

	# Patient DOB
	imgCrop5 = img[745:805,0:420]
	imgList.append(imgCrop5)

	# Patient sex
	imgCrop6 = img[745:805,415:720]
	imgList.append(imgCrop6)

	# Patient Phone No
	imgCrop7 = img[640:720,715:1443]
	imgList.append(imgCrop7)

	# Patient language
	imgCrop5 = img[715:785,715:1443]
	imgList.append(imgCrop5)

	# Patient shipping address
	imgCrop6 = img[795:895,0:720]
	imgList.append(imgCrop6)

	# Patient shipping city
	imgCrop7 = img[885:955,0:720]
	imgList.append(imgCrop7)

	# Patient billing address
	imgCrop6 = img[795:895,715:1433]
	imgList.append(imgCrop6)

	# Patient shipping city
	imgCrop7 = img[885:955,715:1443]
	imgList.append(imgCrop7)


#####################################

	# Patient latino
	imgCrop6 = img[1000:1050,0:1443]
	imgList.append(imgCrop6)

	# Patient race
	imgCrop7 = img[1050:1120,0:1443]
	imgList.append(imgCrop7)	


####################################
	
	# parient has insurance?
	imgCrop5 = img[1180:1235,0:1443]
	imgList.append(imgCrop5)

	# policy holder name
	imgCrop6 = img[1220:1275,0:475]
	imgList.append(imgCrop6)

	# policy holder dob
	imgCrop7 = img[1220:1275,475:835]
	imgList.append(imgCrop7)

	# Relation
	imgCrop6 = img[1220:1275,830:1443]
	imgList.append(imgCrop6)

	# insurance carrier
	imgCrop7 = img[1275:1330,0:605]
	imgList.append(imgCrop7)

	# insurance type
	imgCrop7 = img[1275:1330,600:1443]
	imgList.append(imgCrop7)	

	# insurance address
	imgCrop6 = img[1320:1375,0:1443]
	imgList.append(imgCrop6)

	# policy number
	imgCrop7 = img[1370:1430,0:570]
	imgList.append(imgCrop7)

	# Group
	imgCrop7 = img[1370:1430,570:1000]
	imgList.append(imgCrop7)

	# Plan
	imgCrop7 = img[1370:1430,1000:1443]
	imgList.append(imgCrop7)

	# Autho code
	imgCrop7 = img[1425:1485,0:1443]
	imgList.append(imgCrop7)

	# Final Date
	imgCrop7 = img[1640:1702,950:1443]
	imgList.append(imgCrop7)	
	
	#for img in imgList:
	#	cv.imshow('Window', img)
	#	cv.waitKey(0)
	#	cv.destroyAllWindows()

	return imgList
