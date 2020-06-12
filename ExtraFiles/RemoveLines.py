import numpy as np
import sys
import cv2 as cv

src = cv.imread('aab.png') 

if src is None:
    print ('Error opening image: ' + src)

# Transform source image to gray if it is not already
if len(src.shape) != 2:
    gray = cv.cvtColor(src, cv.COLOR_BGR2GRAY)
else:
    gray = src

# Show gray image
cv.imwrite('image_gray.jpg',gray)

# Apply adaptiveThreshold at the bitwise_not of gray, notice the ~ symbol
gray = cv.bitwise_not(gray)
bw = cv.adaptiveThreshold(gray, 255, cv.ADAPTIVE_THRESH_MEAN_C, cv.THRESH_BINARY, 15, -2)

# Show binary image
cv.imwrite('image_binary.jpg',bw)

# Create the images that will use to extract the horizontal and vertical lines
horizontal = np.copy(bw)
vertical = np.copy(bw)

# Specify size on horizontal axis
cols = horizontal.shape[1]
horizontal_size = cols / 25
horizontal_size=int(horizontal_size)

# Create structure element for extracting horizontal lines through morphology operations
horizontalStructure = cv.getStructuringElement(cv.MORPH_RECT, (horizontal_size, 1))

# Apply morphology operations
horizontal = cv.erode(horizontal, horizontalStructure)
horizontal = cv.dilate(horizontal, horizontalStructure) 


# Show extracted horizontal lines
cv.imwrite('image_horizontal.jpg',horizontal)

# Specify size on vertical axis
rows = vertical.shape[0]
verticalsize = rows / 25
verticalsize = int(verticalsize)

# Create structure element for extracting vertical lines through morphology operations
verticalStructure = cv.getStructuringElement(cv.MORPH_RECT, (1, verticalsize))

# Apply morphology operations
vertical = cv.erode(vertical, verticalStructure)
vertical = cv.dilate(vertical, verticalStructure)

# Show extracted vertical lines
cv.imwrite('image_vertical.jpg',vertical)

# KP Update 1
kp2 = bw - vertical
kp2 = kp2 - horizontal
kp2 = cv.bitwise_not(kp2)
cv.imwrite('image_kp2.jpg',kp2)

# Inverse vertical image
vertical = cv.bitwise_not(vertical)
cv.imwrite('image_vertInverse.jpg',vertical)

# Step 1
edges = cv.adaptiveThreshold(vertical, 255, cv.ADAPTIVE_THRESH_MEAN_C, cv.THRESH_BINARY, 3, -2)
cv.imwrite('image_edges.jpg',edges)

# Step 2
kernel = np.ones((2, 2), np.uint8)
edges = cv.dilate(edges, kernel)
cv.imwrite('image_dilate.jpg',edges)

# Step 3
smooth = np.copy(vertical)

# Step 4
smooth = cv.blur(smooth, (2, 2))

# Step 5
(rows, cols) = np.where(edges != 0)
vertical[rows, cols] = smooth[rows, cols]

# Show final result
cv.imwrite('image_final.jpg',vertical)