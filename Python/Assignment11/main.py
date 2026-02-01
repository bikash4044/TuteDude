import cv2

img = cv2.imread("C:/Users/bikas/Downloads/Highways.jpg",0)

# cv2.imshow("window", img)
print("Shape of image is : ",img.shape)
height, width = img.shape[:2]
width = 685 # new value assigned
dim = (width, height)
resized = cv2.resize(img, dim)

cv2.imshow("window",resized)


cv2.waitKey(2000)

cv2.destroyAllWindows()