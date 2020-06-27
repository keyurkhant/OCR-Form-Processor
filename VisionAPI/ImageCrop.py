import cv2 as cv
import numpy as np
import json
from VisionModule import OCR as ocr
from VisionModule import ROIGeneration as roi
from VisionModule import HoughTransfer as hg
from VisionModule import ContourGenerator as cg
from VisionModule	import PDF2IMG as pi

pdf = open('/root/Keyur Khant/Study/Others/OCR Hackathon/VisionAPI/Untitled-1-converted.pdf' ,'rb').read()

image = pi.toImgList(pdf)

(x, y, w, h) = cg.getContour(image)

img1 = image[y:y+h,x:x+w]

imgList = roi.getROI(img1)

count = 1
finaldict = {}
for img in imgList:	
	if(count == 3):
		img = cg.getRect(img)
	text = ocr.Text_Recognize(img)
	finaldict[count] = text
	count += 1
	cv.imshow('winodw', img)


with open('/root/Keyur Khant/Study/Others/OCR Hackathon/VisionAPI/text.json', 'w') as file:
	file.write(json.dumps(finaldict))
file.close()

print("Done")
cv.waitKey(0)
cv.destroyAllWindows()



