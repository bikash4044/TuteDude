import cv2
import numpy as np

img = cv2.imread("C:/Users/bikas/Downloads/Highways.jpg",0)
width = 650
height = 850
dim = (width,height)
resized = cv2.resize(img, dim)

flip = cv2.flip(resized,1)
flip_0 = cv2.flip(resized,0)
flip_1 = cv2.flip(resized,-1)

cv2.imshow("Original",resized)
# cv2.imshow("Horizontal",flip)
# cv2.imshow("Vertical",flip_0)
cv2.imshow("Horizontal and vertical flip",flip_1)
cv2.waitKey(0)
cv2.destroyAllWindows()
