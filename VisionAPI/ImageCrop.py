import cv2 as cv
import numpy as np
from VisionModule	import PDF2IMG as pi
from VisionModule import recognize

pdf = open('/root/Keyur Khant/Study/Others/OCR Hackathon/FilledForm.pdf' ,'rb').read()

image = pi.toImgList(pdf)

data = recognize.recognize(image)


