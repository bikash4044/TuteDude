import cv2
import numpy as np
img = cv2.imread("C:/Users/bikas/Downloads/Highways.jpg",0)
column,row = img.shape[:2]

threshold_value = 200

_,binary_threshold = cv2.threshold(img,threshold_value,255,cv2.THRESH_BINARY)

cv2.imshow("Original",img)
cv2.imshow("Threshold",binary_threshold)
cv2.waitKey(0)
cv2.destroyAllWindows()