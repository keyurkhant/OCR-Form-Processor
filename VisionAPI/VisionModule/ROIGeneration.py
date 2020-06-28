import cv2 as cv
import numpy as np
from pdf2image import convert_from_bytes


def getROI(img):
	
	#standard Pixel for this
	img = cv.resize(img , (1443 , 1702))

	cv.imwrite('output.jpg' , img)
	imgList = []

	# HCO Name
	imgCrop1 = img[100:172,380:718]
	imgList.append(imgCrop1)

	# Provider Name
	imgCrop2 = img[160:233,198:718] 
	imgList.append(imgCrop2)	

	# NPI Number
	imgCrop3 = img[226:320,88:718]
	imgList.append(imgCrop3)

	# Provider Address 
	imgCrop4 = img[310:380,223:718]
	imgList.append(imgCrop4)

	# Provider City
	imgCrop5 = img[370:440,188:718]
	imgList.append(imgCrop5)

	# Provider Phone
	imgCrop6 = img[430:500,203:718]
	imgList.append(imgCrop6)

	# Provider Fax
	imgCrop7 = img[490:560,263:718]
	imgList.append(imgCrop7)




#################################

	# ICD 10 code (if Others then)
	imgCrop3 = img[297:360,855:1420]
	imgList.append(imgCrop3)

	# Date of order 
	imgCrop4 = img[513:562,1110:1420]
	imgList.append(imgCrop4)

#################################

	# Patient ID
	imgCrop5 = img[650:710,205:718]
	imgList.append(imgCrop5)

	# Patient first name
	imgCrop6 = img[695:750,148:313]
	imgList.append(imgCrop6)

	# Patient Last Name
	imgCrop7 = img[695:750,450:718]
	imgList.append(imgCrop7)

	# Patient DOB
	imgCrop5 = img[745:795,243:425]
	imgList.append(imgCrop5)

	# Patient sex
	imgCrop6 = img[745:795,475:720]
	imgList.append(imgCrop6)

	# Patient Phone No
	imgCrop7 = img[650:696,1053:1420]
	imgList.append(imgCrop7)
 
	# Patient Phone No type
	imgCrop8 = img[690:720,1053:1420]
	imgList.append(imgCrop8)

	# Patient language
	imgCrop5 = img[715:785,1123:1420]
	imgList.append(imgCrop5)

	# Patient shipping address
	imgCrop6 = img[800:910,228:718]
	imgList.append(imgCrop6)

	# Patient shipping city
	imgCrop7 = img[895:950,203:718]
	imgList.append(imgCrop7)

	# Patient billing address
	imgCrop6 = img[795:910,933:1420]
	imgList.append(imgCrop6)

	# Patient billing city
	imgCrop7 = img[895:950,923:1420]
	imgList.append(imgCrop7)


#####################################

	# Patient latino
	imgCrop6 = img[1000:1050,640:840]
	imgList.append(imgCrop6)

	# Patient race
	imgCrop7 = img[1075:1118,10:1420]
	imgList.append(imgCrop7)	


####################################
	
	# parient has insurance?
	imgCrop5 = img[1190:1235,668:1420]
	imgList.append(imgCrop5)

	# policy holder name
	imgCrop6 = img[1225:1285,242:475]
	imgList.append(imgCrop6)

	# policy holder dob
	imgCrop7 = img[1225:1285,685:825]
	imgList.append(imgCrop7)

	# Relation
	imgCrop6 = img[1225:1285,1105:1425]
	imgList.append(imgCrop6)

	# insurance carrier
	imgCrop7 = img[1270:1340,318:605]
	imgList.append(imgCrop7)

	# insurance type
	imgCrop7 = img[1270:1340,666:1430]
	imgList.append(imgCrop7)	

	# insurance address
	imgCrop6 = img[1325:1385,336:1430]
	imgList.append(imgCrop6)

	# policy number
	imgCrop7 = img[1370:1440,353:565]
	imgList.append(imgCrop7)

	# Group
	imgCrop7 = img[1370:1440,748:1005]
	imgList.append(imgCrop7)

	# Plan
	imgCrop7 = img[1370:1440,1068:1430]
	imgList.append(imgCrop7)

	# Autho code
	imgCrop7 = img[1420:1475,453:1400]
	imgList.append(imgCrop7)

	# Final Date
	imgCrop7 = img[1640:1687,1020:1343]
	imgList.append(imgCrop7)	
	
	return imgList

