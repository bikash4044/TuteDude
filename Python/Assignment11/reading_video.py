import cv2

video = cv2.VideoCapture("C:/Users/bikas/Downloads/video.mp4")
while video.isOpened():
    _,fame = video.read()
    frame = cv2.resize(fame,(800,720))
    cv2.imshow("frame",frame)


    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cv2.destroyAllWindows()