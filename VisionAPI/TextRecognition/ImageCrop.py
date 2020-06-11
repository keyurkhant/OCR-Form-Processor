import cv2 as cv
import numpy as np
from VisionModule import OCR as ocr
from VisionModule import ROIGeneration as roi

pdf = open('/root/Keyur Khant/Study/Others/OCR Hackathon/sampleform.pdf' ,'rb').read()

list1 = roi.getROI(pdf)

print(ocr.Text_Recognize(list1[4]))

cv.waitKey(0)
cv.destroyAllWindows()