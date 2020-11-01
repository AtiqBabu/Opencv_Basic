import cv2
import numpy as np

circles = np.zeros((4,2), np.int)
counter = 0

def mousePoint(event, x, y, flags, params):
    global counter
    if event == cv2.EVENT_LBUTTONDOWN:
        print(x, y)
        circles[counter] = x,y
        counter = counter + 1
        print(circles)

path = "Resources/cardd.jpg"
img = cv2.imread(path)
width, height = 250, 350
while True:
    if counter == 4:
        pts1 = np.float32([circles[0], circles[1], circles[2], circles[3]])
        pts2 = np.float32([[0,0], [width,0], [0, height], [width, height]])
        matrix = cv2.getPerspectiveTransform(pts1, pts2)
        imgOutput = cv2.warpPerspective(img, matrix, (width, height))
        cv2.imshow("Output Image", imgOutput)

    #print(pts1)
    for x in range (0,4):
        cv2.circle(img, (circles[x][0], circles[x][1]), 3, (0,0,255), cv2.FILLED)

    cv2.imshow("Original Image", img)
    cv2.setMouseCallback("Original Image", mousePoint)
    cv2.waitKey(1)