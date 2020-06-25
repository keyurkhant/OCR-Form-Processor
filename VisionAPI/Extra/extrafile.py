import cv2 as cv
import numpy as np
from pdf2image import convert_from_bytes

def getROI():
	pdf = open('/root/Keyur Khant/Study/Others/OCR Hackathon/VisionAPI/final_10_400ppi.pdf' ,'rb').read()
	images = convert_from_bytes(pdf)
	img = images[0]
	img = np.array(img)
	
	cv.imwrite('main.jpg', img)

getROI()