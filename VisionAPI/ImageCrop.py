import cv2 as cv
import numpy as np
from VisionModule import OCR as ocr
from VisionModule import ROIGeneration as roi
from VisionModule import HoughTransfer as hg
from VisionModule import ContourGenerator as cg
from VisionModule	import PDF2IMG as pi

pdf = open('/root/Keyur Khant/Study/Others/OCR Hackathon/VisionAPI/final_10_400ppi.pdf' ,'rb').read()

image = pi.toImgList(pdf)
#image = cv.imread('/root/Keyur Khant/Study/Others/OCR Hackathon/VisionAPI/Untitled-3.jpg')

(x, y, w, h) = cg.getContour(image)

img1 = image[y:y+h,x:x+w]

imglist = roi.getROI(img1)

count = 1

for img in imglist:	
	#img = hg.imagePurify(img)
	text = ocr.Text_Recognize(img)
	cv.imwrite('/root/Keyur Khant/Study/Others/OCR Hackathon/VisionAPI/result/img'+str(count)+'.jpg' , img)
	file = open('/root/Keyur Khant/Study/Others/OCR Hackathon/VisionAPI/result/text'+str(count)+'.txt' , 'a')
	file.write(text)
	file.close()
	count += 1

print("Done")
cv.waitKey(0)
cv.destroyAllWindows()



