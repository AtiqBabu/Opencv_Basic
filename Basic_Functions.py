import cv2
import numpy as np

kernel = np.ones((5,5), np.uint8)

path = "Resources/lena.png"
img = cv2.imread(path)
#grayImg = cv2.imread(path, 0) # 0 refers gray images
grayImage = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
blurImg = cv2.GaussianBlur(grayImage, (7,7), 0) #kernel size(7,7) refers depth of blur
cannyImage = cv2.Canny(blurImg, 100, 200)# thresold value refers amount of canny
dilatedImage = cv2.dilate(cannyImage, kernel, iterations=1) #iteration refers amount of selection
erodedImg = cv2.erode(dilatedImage, kernel, iterations=1) #reverse of dilated image


##########Showing Images ##########
cv2.imshow("Original Image", img)
cv2.imshow("Gray Scale Image", grayImage)
cv2.imshow("Blur Image", blurImg)
cv2.imshow("canny Image", cannyImage)
cv2.imshow("Dilated Image", dilatedImage)
cv2.imshow("Eroded Image", erodedImg)
cv2.waitKey(0)