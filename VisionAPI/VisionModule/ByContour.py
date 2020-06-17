import cv2

BLUR = 21
CANNY_THRESH_1 = 10
CANNY_THRESH_2 = 200
MASK_DILATE_ITER = 10
MASK_ERODE_ITER = 10
MASK_COLOR = (0.0,0.0,0.0) # In BGR format\

img = cv2.imread('Original/sampleform-1.jpg')
img = cv2.resize(img, (780, 540), interpolation = cv2.INTER_NEAREST) 
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
#gray1 = gray.copy()

#_, th1 = cv2.threshold(gray,198, 255, cv2.THRESH_BINARY)

edges = cv2.Canny(gray,CANNY_THRESH_1, CANNY_THRESH_2)
edges = cv2.dilate(edges, None)
edges = cv2.erode(edges, None)

cv2.imshow('image', edges)
cv2.waitKey(0)
cv2.destroyAllWindows()

contour_info = []
contours, hierarchy = cv2.findContours(edges, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

for c in contours:
    contour_info.append((c, cv2.isContourConvex(c), cv2.contourArea(c),))
contour_info = sorted(contour_info, key=lambda c: c[2], reverse=True)

#max_contour = contour_info[0]
#(x, y, w, h) = cv2.boundingRect(max_contour[0])
#cv2.rectangle(img, (x,y), (x+w, y+h), (255, 0, 0), 2)
k = 0
for i in contour_info:
    (x, y, w, h) = cv2.boundingRect(i[0])
    cv2.rectangle(img, (x,y), (x+w, y+h), (255, 0, 0), 2)
    
    print(i[2])
    
    cv2.imshow('image', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    
    k += 1
    if k > 15:
        break
    
print(k)

#cv2.rectangle(img, (x,y), (x+w, y+h), (255, 0, 0), 2)

cv2.imshow('image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()