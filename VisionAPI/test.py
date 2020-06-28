import cv2
import numpy as np
from VisionModule import recorgnize

image = cv2.imread('static/temp_storage/Untitled-2.jpg')
data = recorgnize.recorgnize(image)


