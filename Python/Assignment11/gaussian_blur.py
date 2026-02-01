import cv2
import numpy as np
img = cv2.imread("C:/Users/bikas/Downloads/Highways.jpg",0)
column,row = img.shape[:2]

resized_img = cv2.resize(img,(column,row))
ksize = (7,7)
sigmax = 0
sigmay = 0
blur = cv2.GaussianBlur(resized_img,ksize,0)
cv2.imshow("Original",resized_img)
cv2.imshow("blur",blur)
cv2.waitKey(0)
cv2.destroyAllWindows()