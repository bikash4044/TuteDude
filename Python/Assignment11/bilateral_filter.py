import cv2
import numpy as np
img = cv2.imread("C:/Users/bikas/Downloads/Highways.jpg",0)
column,row = img.shape[:2]

resized_img = cv2.resize(img,(column,row))

d = 7
sigmacolor = 100
sigmaspace = 100

b = cv2.bilateralFilter(resized_img,d,sigmacolor,sigmaspace)

cv2.imshow("Original",resized_img)
cv2.imshow("Output",b)
cv2.waitKey(0)
cv2.destroyAllWindows()