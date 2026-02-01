import cv2

img = cv2.imread("C:/Users/bikas/Downloads/Highways.jpg")

print(img.size, " is the image size in bytes")
print("Dimension is ", img.shape)

scale = 150

width = int(img.shape[1] * scale/100)
height = int(img.shape[0] * scale/100)
dim = (width, height)

resized = cv2.resize(img, dim, interpolation = cv2.INTER_AREA)
print("Dimension of resized image is ", resized.shape)

cv2.imshow("Original", img)
cv2.imshow("Resized", resized)
cv2.waitKey(0)
cv2.destroyAllWindows()