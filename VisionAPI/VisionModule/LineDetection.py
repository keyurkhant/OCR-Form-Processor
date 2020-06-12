import cv2
import numpy as np

img = cv2.imread('Original/sampleform.png')
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
edges = cv2.Canny(gray,50,150,apertureSize = 3)

lines = cv2.HoughLines(edges,1,np.pi/180,200)

print(lines.shape)
print(lines[0].shape)
for line in lines:
    for rho, theta in line:
        a = np.cos(theta)
        b = np.sin(theta)
        x0 = a*rho
        y0 = b*rho
        x1 = int(x0 + 1000*(-b))
        y1 = int(y0 + 1000*(a))
        x2 = int(x0 - 1000*(-b))
        y2 = int(y0 - 1000*(a))
        print(theta)
        
        if theta == 0 and rho > 300 and rho < 500:
            print(rho)
            cv2.line(img,(x1,y1),(x2,y2),(255,255,255),1)
        if theta > 1.55 and theta < 1.58:
            cv2.line(img,(x1,y1),(x2,y2),(0,0,0),1)

cv2.imwrite('Original/removedLine.jpg',img)
cv2.imshow('image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()