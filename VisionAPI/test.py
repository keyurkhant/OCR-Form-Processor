from VisionModule import OCR as ocr
from VisionModule import HoughTransfer as hg
from VisionModule import ContourGenerator as cg
import cv2 as cv


img = cv.imread('/root/Keyur Khant/Study/Others/OCR Hackathon/VisionAPI/result/img3.19.jpg')

img = cg.getRect(img)
text = ocr.Text_Recognize(img)


print(text)
cv.imshow('Window',img)
cv.waitKey(0)
cv.destroyAllWindows()

