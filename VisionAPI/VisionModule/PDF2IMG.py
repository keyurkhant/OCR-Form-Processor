import cv2 as cv
import numpy as np
from pdf2image import convert_from_bytes

def toImg(pdf):
	pdf.save('static/temp_storage/'+pdf.filename)
	full = open('static/temp_storage/'+pdf.filename,'rb').read()
	images = convert_from_bytes(full)
	if(len(images) == 1):
		img1 = np.array(images[0])
		cv.imwrite('static/temp_storage/'+pdf.filename+'1.jpg', img1)
		return [img1]
	else:
		img1 = np.array(images[0])
		cv.imwrite('static/temp_storage/'+pdf.filename+'1.jpg', img1)
		img2 = np.array(images[1])
		cv.imwrite('static/temp_storage/'+pdf.filename+'2.jpg', img2)
		return [img1, img2]

def toImgList(pdf):
	images = convert_from_bytes(pdf)
	if(len(images) == 1):
		img1 = np.array(images[0])
		return [img1]
	else:
		img1 = np.array(images[0])
		img2 = np.array(images[1])
		return [img1, img2]