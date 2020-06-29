import cv2 as cv
import numpy as np
from pdf2image import convert_from_bytes
import time

def toImg(pdf):
	pdf.save('static/temp_storage/'+pdf.filename)
	full = open('static/temp_storage/'+pdf.filename,'rb').read()
	images = convert_from_bytes(full)
	img1 = images[0]
	img1 = np.array(img1)
	cv.imwrite('static/temp_storage/'+pdf.filename+'1.jpg', img1)
	img2 = images[1]
	img2 = np.array(img2)
	cv.imwrite('static/temp_storage/'+pdf.filename+'2.jpg', img2)