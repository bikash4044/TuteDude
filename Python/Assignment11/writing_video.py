import cv2

video = cv2.VideoCapture("C:/Users/bikas/Downloads/video.mp4")

fourcc = cv2.VideoWriter_fourcc(*'mp4v')
# try:
#     frame_width = int(video.get(cv2.CAP_PROP_FRAME_WIDTH))
#     frame_height = int(video.get(cv2.CAP_PROP_FRAME_HEIGHT))
#     print("Frame width:",frame_width,"Frame height:",frame_height)
# except:
#     pass
output = cv2.VideoWriter('output.mp4', fourcc, 25.0, (640,360))

while video.isOpened():
    ret, frame = video.read()
    if ret == True:
        output.write(frame)
        cv2.imshow('frame',frame)

        if  cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break

cv2.destroyAllWindows()