# Import required libraries and modules
import cv2
import numpy as np
from datetime import datetime


def removeLine(img):
    '''
    This function take an argument as image(numpy array)

    Hough Line transform is technique to detect line 
    (even if shortly broken) in computer vision.

    It detect lines and remove it. (Here apply white color.) and return image(processed)
    '''
    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY) # Convert image into grayscale
    
    # This both line detect lines in image
    edges = cv2.Canny(gray,50,150,apertureSize = 3)      
    lines = cv2.HoughLines(edges,1,np.pi/180, 50) 

    for line in lines:
        for r, theta in line: 
        
            a = np.cos(theta) 
            b = np.sin(theta) 
            
            x0 = a*r 
            
            # y0 stores the value rsin(theta) 
            y0 = b*r 
            
            # x1 stores the rounded off value of (rcos(theta)-1000sin(theta)) 
            x1 = int(x0 + 1000*(-b)) 
            
            # y1 stores the rounded off value of (rsin(theta)+1000cos(theta)) 
            y1 = int(y0 + 1000*(a)) 
        
            # x2 stores the rounded off value of (rcos(theta)+1000sin(theta)) 
            x2 = int(x0 - 1000*(-b)) 
            
            # y2 stores the rounded off value of (rsin(theta)-1000cos(theta)) 
            y2 = int(y0 - 1000*(a)) 
            
            if (theta < 0.05 and theta > -0.05) or (theta > 1.56 and theta < 1.58):
                cv2.line(img,(x1,y1), (x2,y2), (255,255,255),5)
                 
    return img


def removeBox(img):
    '''
    This function take an argument as image(numpy array)

    Contour finding method used for find contour(Rectangle box)
    in image. It's time complexity is less that HoughLine Transform 
 
    It detect all rectangle.
    '''
    BLUR = 21
    CANNY_THRESH_1 = 10
    CANNY_THRESH_2 = 200
    MASK_DILATE_ITER = 10
    MASK_ERODE_ITER = 10
    MASK_COLOR = (0.0,0.0,0.0) # In BGR format

    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY) # Convert image into grayscale 

    edges = cv2.Canny(gray,CANNY_THRESH_1, CANNY_THRESH_2)
    edges = cv2.dilate(edges, None)
    edges = cv2.erode(edges, None)

    # Detect contour using findContours method
    contour_info = []
    contours, hierarchy = cv2.findContours(edges, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    for c in contours:
        contour_info.append((c, cv2.isContourConvex(c), cv2.contourArea(c),))
    contour_info = sorted(contour_info, key=lambda c: c[2], reverse=True)
    
    for i in contour_info:
        (x, y, w, h) = cv2.boundingRect(i[0])
        if i[2] < 2500:
            break
        cv2.rectangle(img, (x,y), (x+w, y+h), (255, 255, 255), 5)   # It take all rectange and put white color.
        
    return img
