####################################
import cv2
import numpy

####################################

frameWidth = 640
frameHeight = 480

cap = cv2.VideoCapture(0)
cap.set(3, frameWidth)
cap.set(4, frameHeight)

while True:
    success, img = cap.read()
    cv2.imshow("video", img)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break