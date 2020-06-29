import cv2 as cv
import numpy as np
from pdf2image import convert_from_bytes

def getROI():
	
	img = cv.imread('/root/Keyur Khant/Study/Others/OCR Hackathon/VisionAPI/VisionModule/result4/img1.jpg')
	
	#standard Pixel for this
	img = cv.resize(img , (1443 , 1702))

	cv.imwrite('output.jpg' , img)
	imgList = []

	# HCO Name
	imgCrop1 = img[100:172,368:718]
	imgList.append(imgCrop1)

	# Provider Name
	imgCrop2 = img[160:233,190:718] 
	imgList.append(imgCrop2)	

	# NPI Number
	imgCrop3 = img[226:320,80:718]
	imgList.append(imgCrop3)

	# Provider Address 
	imgCrop4 = img[310:380,215:718]
	imgList.append(imgCrop4)

	# Provider City
	imgCrop5 = img[370:440,180:718]
	imgList.append(imgCrop5)

	# Provider Phone
	imgCrop6 = img[430:500,195:718]
	imgList.append(imgCrop6)

	# Provider Fax
	imgCrop7 = img[490:560,255:718]
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
	imgCrop5 = img[650:710,200:718]
	imgList.append(imgCrop5)

	# Patient first name
	imgCrop6 = img[695:750,140:313]
	imgList.append(imgCrop6)

	# Patient Last Name
	imgCrop7 = img[695:750,442:718]
	imgList.append(imgCrop7)

	# Patient DOB
	imgCrop5 = img[745:795,235:420]
	imgList.append(imgCrop5)

	# Patient sex
	imgCrop6 = img[745:795,467:720]
	imgList.append(imgCrop6)

	# Patient Phone No
	imgCrop7 = img[650:720,1045:1420]
	imgList.append(imgCrop7)

	# Patient language
	imgCrop5 = img[715:785,1115:1420]
	imgList.append(imgCrop5)

	# Patient shipping address
	imgCrop6 = img[800:910,220:718]
	imgList.append(imgCrop6)

	# Patient shipping city
	imgCrop7 = img[895:950,195:718]
	imgList.append(imgCrop7)

	# Patient billing address
	imgCrop6 = img[795:910,925:1420]
	imgList.append(imgCrop6)

	# Patient billing city
	imgCrop7 = img[895:950,915:1420]
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
	imgCrop5 = img[1190:1235,660:1420]
	imgList.append(imgCrop5)

	# policy holder name
	imgCrop6 = img[1225:1285,236:475]
	imgList.append(imgCrop6)

	# policy holder dob
	imgCrop7 = img[1225:1285,685:825]
	imgList.append(imgCrop7)

	# Relation
	imgCrop6 = img[1225:1285,1105:1425]
	imgList.append(imgCrop6)

	# insurance carrier
	imgCrop7 = img[1270:1340,315:605]
	imgList.append(imgCrop7)

	# insurance type
	imgCrop7 = img[1270:1340,666:1430]
	imgList.append(imgCrop7)	

	# insurance address
	imgCrop6 = img[1325:1385,333:1430]
	imgList.append(imgCrop6)

	# policy number
	imgCrop7 = img[1370:1440,350:565]
	imgList.append(imgCrop7)

	# Group
	imgCrop7 = img[1370:1440,745:1005]
	imgList.append(imgCrop7)

	# Plan
	imgCrop7 = img[1370:1440,1065:1430]
	imgList.append(imgCrop7)

	# Autho code
	imgCrop7 = img[1420:1475,450:1400]
	imgList.append(imgCrop7)

	# Final Date
	imgCrop7 = img[1640:1687,1020:1343]
	imgList.append(imgCrop7)	
	
	return imgList

