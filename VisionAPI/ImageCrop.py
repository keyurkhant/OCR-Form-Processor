import cv2 as cv
import numpy as np
from VisionModule	import PDF2IMG as pi
from VisionModule import recognize
from VisionModule import OCR as ocr
from VisionModule import ContourGenerator as cg
from VisionModule import ROIGeneration as roi
from VisionModule import removeNoise as rn  # Text processing 1
from VisionModule import replace #  Text processing 2

#pdf = open('/root/Keyur Khant/Study/Others/OCR Hackathon/VisionAPI/sampleform-2-converted.pdf' ,'rb').read()

#image = pi.toImg(pdf)

image = cv.imread('/root/Keyur Khant/Study/Others/OCR Hackathon/VisionAPI/sampleform-2.jpg')

(x, y, w, h) = cg.getContour(image) # Generate Contour and return it's X & Y points.
img1 = image[y:y+h,x:x+w]

imgList = roi.getSecondROI(img1)

text = ocr.Text_Recognize(imgList[0])
text = replace.replaceNum(text)
print(text)

text = ocr.Text_Recognize(imgList[1])
text = replace.handleDate(text)
print(text)




