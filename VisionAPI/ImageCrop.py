import cv2 as cv
import numpy as np
from VisionModule import OCR as ocr
from VisionModule import ROIGeneration as roi
from VisionModule import HoughTransfer as hg


pdf = open('sampleform.pdf' ,'rb').read()

list1 = roi.getROI(pdf)
count = 1

list1[7] = cv.resize(list1[7] , (772, 577))

for img in list1:	
	img = hg.imagePurify(img)
	text = ocr.Text_Recognize(img)
	cv.imwrite('img'+str(count)+'.jpg' , img)
	file = open('text'+str(count)+'.txt' , 'a')
	file.write(text)
	file.close()
	count += 1

print("Done")
cv.waitKey(0)
cv.destroyAllWindows()



