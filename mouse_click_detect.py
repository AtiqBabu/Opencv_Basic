import cv2
import numpy as np

def mousePoint(event, x, y, flags, params):
    if event == cv2.EVENT_LBUTTONDOWN :
        print(x, y)

path = "Resources/card.png"
img = cv2.imread(path)

cv2.imshow("Original Image", img)
cv2.setMouseCallback("Original Image", mousePoint)

cv2.waitKey(0)