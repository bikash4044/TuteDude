import cv2
import numpy as np
img = cv2.imread("C:/Users/bikas/Downloads/Highways.jpg")
column,row = img.shape[:2]

center = (column//2,row//2)
angle = 90

r = cv2.getRotationMatrix2D(center,angle,1)

rotate = cv2.warpAffine(img,r,(column,row))

cv2.imshow("img",img)
cv2.imshow("rotated",rotate)
cv2.waitKey(0)
cv2.destroyAllWindows()