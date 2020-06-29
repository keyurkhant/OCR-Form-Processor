# Import OpenCV-Python library
import cv2

BLUR = 21
CANNY_THRESH_1 = 10
CANNY_THRESH_2 = 200
MASK_DILATE_ITER = 10
MASK_ERODE_ITER = 10
MASK_COLOR = (0.0,0.0,0.0) # In BGR format


def getContour(img):
    '''
    This function take an argument as image(numpy array)

    Contour Generation find all rectangle from image and
    return largest rectangle (X,Y,W,H) which we required.
    '''    
    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY) # Convert into grayscale

    edges = cv2.Canny(gray,CANNY_THRESH_1, CANNY_THRESH_2)  # Canny for line detection
    edges = cv2.dilate(edges, None)
    edges = cv2.erode(edges, None)

    contour_info = []
    contours, hierarchy = cv2.findContours(edges, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE) # Find contour

    for c in contours:
        contour_info.append((c, cv2.isContourConvex(c), cv2.contourArea(c),)) # Take each contour and find area
    contour_info = sorted(contour_info, key=lambda c: c[2], reverse=True) # Sort contour by area

    k = 0
    imgList = []

    i = contour_info[0]
    (x, y, w, h) = cv2.boundingRect(i[0]) # Return X,Y,W,H of largest area contour
    
    return (x, y, w, h)