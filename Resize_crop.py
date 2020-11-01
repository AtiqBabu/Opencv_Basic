import cv2

path = "Resources/road.jpg"
img = cv2.imread(path)

print(img.shape)
###Resize an image
width, height = 900, 549
imgResize = cv2.resize(img, (width, height))
print(imgResize.shape)
#imgCropped = imgResize[300:540, 0:900] #height, width
imgCropped = imgResize[300:540, 400:470] #height, width
imgCroppedResize = cv2.resize(imgCropped, (imgResize.shape[1], imgResize.shape[0]))

#cv2.imshow("Original Image", img)
cv2.imshow("Resized Image", imgResize)
cv2.imshow("Cropped Image", imgCropped)
cv2.imshow("Cropped Resize Image", imgCroppedResize)
cv2.waitKey(0)