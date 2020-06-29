# Import required libraries
import cv2 as cv
import numpy as np
from pdf2image import convert_from_bytes

def toImg(pdf):
	'''
	This function takes an argument as pdf file, converts into 
	images of it's pages and store temporary in local storage,	
	and return image list.(numpy array)
	'''
	pdf.save('static/temp_storage/'+pdf.filename)	# Save pdf file
	full = open('static/temp_storage/'+pdf.filename,'rb').read()	# Take pdf file as byte wise object
	images = convert_from_bytes(full)	# Convert into images
	# If only one image (Cologuard form given only)
	if(len(images) == 1):
		img1 = np.array(images[0])
		cv.imwrite('static/temp_storage/'+pdf.filename+'1.jpg', img1) # Save image
		return [img1]
	# If two pages into pdf
	else:
		img1 = np.array(images[0])
		cv.imwrite('static/temp_storage/'+pdf.filename+'1.jpg', img1)
		img2 = np.array(images[1])
		cv.imwrite('static/temp_storage/'+pdf.filename+'2.jpg', img2)
		return [img1, img2]
