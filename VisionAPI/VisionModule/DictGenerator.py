import cv2 as cv
import numpy as np
from VisionModule import OCR as ocr
from VisionModule import ROIGeneration as roi
from VisionModule import HoughTransfer as hg
from VisionModule import ContourGenerator as cg
from VisionModule	import PDF2IMG as pi

def getDict(pdf):
	images = pi.toImgList(pdf)

	# First Image Main Contour Crop
	(x, y, w, h) = cg.getContour(images)
	#Crop the image
	img = firstimg[y:y+h,x:x+w]

	imgList = roi.getROI(img) # Get All ROI of Images (small Segments)

	count = 1

	finaldict = {}
	for img in imgList:	
		if(count == 3):
			img = hg.imagePurify(img)
		text = ocr.Text_Recognize(img)
		finaldict[count] = text
		count += 1

	file = open('/root/Keyur Khant/Study/Others/OCR Hackathon/VisionAPI/text.txt', 'a')
	file.write(finaldict)
	file.close()



pdf = open('/root/Keyur Khant/Study/Others/OCR Hackathon/VisionAPI/final_10_400ppi.pdf' ,'rb').read()

getDict(pdf)