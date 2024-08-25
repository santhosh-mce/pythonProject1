import cv2 as cv

img = cv.imread("Resources\Photos\cat.jpg")

cv.imshow("Cat", img)

# capture = cv.VideoCapture('Resources\Videos\dog.mp4')
#
# while True:
#     ret, frame = capture.read()
#     cv.imshow('Video', frame)
#
#     if cv.waitKey(1) & 0xFF == ord('q'):
#         break
#
# capture.release()
# cv.destroyAllWindows()

cv.waitKey(0)