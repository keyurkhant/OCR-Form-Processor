import cv2
import time

BLUR = 21
CANNY_THRESH_1 = 10
CANNY_THRESH_2 = 200
MASK_DILATE_ITER = 10
MASK_ERODE_ITER = 10
MASK_COLOR = (0.0,0.0,0.0) # In BGR format\


def getContour(img):    
    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

    edges = cv2.Canny(gray,CANNY_THRESH_1, CANNY_THRESH_2)
    edges = cv2.dilate(edges, None)
    edges = cv2.erode(edges, None)

    contour_info = []
    contours, hierarchy = cv2.findContours(edges, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    for c in contours:
        contour_info.append((c, cv2.isContourConvex(c), cv2.contourArea(c),))
    contour_info = sorted(contour_info, key=lambda c: c[2], reverse=True)

    k = 0
    imgList = []

    i = contour_info[0]
    (x, y, w, h) = cv2.boundingRect(i[0])
    
    #cv2.rectangle(img, (x,y), (x+w, y+h), (255, 0, 0), 3)
    
    #cv2.imshow('temp', img)
    #cv2.waitKey(0)
    #cv2.destroyAllWindows()
    #
    #cv2.imshow('temp', img[y:y+h, x:x+w])
    #cv2.waitKey(0)
    #cv2.destroyAllWindows()
    

    #for i in contour_info:
    #    (x, y, w, h) = cv2.boundingRect(i[0])
    #    cv2.rectangle(img, (x,y), (x+w, y+h), (255, 255, 255), 3)
    #    imgList.append(img[y:y+h ,x:x+w])
    #    
    #    k += 1
    #    if k > 37:
    #        break

    return (x, y, w, h)