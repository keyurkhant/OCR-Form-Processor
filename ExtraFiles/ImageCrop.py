import cv2 as cv
import numpy as np
from VisionAPI.OCR import OCR as ocr

img = cv.imread('sampleform-1.jpg')
img2 = cv.imread('sampleform-2.jpg')

#Provider Information Form 1
imgCrop1 = img[270:860,60:850]
#cv.imwrite("Crop1.png", imgCrop1)

# Order Information Form 1
imgCrop2 = img[270:860,840:1650] 
#cv.imwrite("Crop2.png", imgCrop2)

# Patient Demographic 1 Form 1
imgCrop3 = img[910:1250,60:850]
#cv.imwrite("Crop3.png", imgCrop3)

# Patient Demographic 2 Form 1
imgCrop4 = img[910:1250,840:1650]
#cv.imwrite("Crop4.png", imgCrop4)

# Patient Ethinicity Form 1
imgCrop5 = img[1250:1430,60:1650]
#cv.imwrite("Crop5.png", imgCrop5)

# Patient Insurance Form 1
imgCrop6 = img[1440:1820,60:1650]
#cv.imwrite("Crop6.png", imgCrop6)

# For lab use only Form 1
imgCrop7 = img[2050:2150,1050:1650]
#cv.imwrite("Crop7.png", imgCrop7)

# Form 2 (Only One Region)
imgCrop8 = img2[685:1800,90:1600]
#cv.imwrite("Crop8.png", imgCrop8)

kp = ocr.Text_Recognize(imgCrop8)

print(kp)


cv.waitKey(0)
cv.destroyAllWindows()