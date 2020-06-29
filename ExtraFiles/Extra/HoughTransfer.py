import numpy as np
import cv2


#gray = cv2.resize(gray , (772, 577))

def imagePurify(img):
    edges = cv2.Canny(img,50,150,apertureSize = 3)

    minLineLength=100
    lines = cv2.HoughLinesP(image=edges,rho=1,theta=np.pi/180, threshold=320,lines=np.array([]), minLineLength=minLineLength,maxLineGap=80)

    a,b,c = lines.shape
    for i in range(a):
        cv2.line(img, (lines[i][0][0], lines[i][0][1]), (lines[i][0][2], lines[i][0][3]), (255, 255, 255), 2, cv2.LINE_AA)
    
    return img
