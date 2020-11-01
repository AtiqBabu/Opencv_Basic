import cv2

#################################

img = cv2.imread('Resources/lena.png')

################################

##############  showing image  ###################

cv2.imshow("Image", img)
cv2.waitKey(0)

##############    End Image    ##################