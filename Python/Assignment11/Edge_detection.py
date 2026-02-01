import cv2
import numpy as np
img = cv2.imread("C:/Users/bikas/Downloads/Highways.jpg",0)
column,row = img.shape[:2]

resized_img = cv2.resize(img,(column,row))

min_thresh = 100
max_thresh = 200
edges  = cv2.Canny(resized_img,min_thresh,max_thresh)

cv2.imshow("Original",resized_img)
cv2.imshow("Edges",edges)
cv2.waitKey(0)
cv2.destroyAllWindows()