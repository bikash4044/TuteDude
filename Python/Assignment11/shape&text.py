import cv2
import numpy as np
img2 = cv2.imread("C:/Users/bikas/Downloads/Highways.jpg")
img = np.zeros(shape = [600,800,3], dtype="uint8")
cv2.line(img,(150,150),(250,250),(120,100,255),2)
cv2.rectangle(img,(800,800),(400,400),(0,0,255),2)
cv2.circle(img,(500,500),100,(0,0,255),2)

pts_polygon = np.array([[300,300],[150,280],[0,0],[230,540],[190,0],[0,230],[300,300],[100,100]])
cv2.polylines(img,[pts_polygon],True,(0,0,255),2)

font = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(img, "Hello there", (400,300), font, 2, (0,0,255), 2, cv2.LINE_AA)

cv2.imshow("img",img)
cv2.waitKey(0)
cv2.destroyAllWindows()