import cv2
import numpy as np
 
img = cv2.imread("pics/picture.PNG")
kernel = np.ones((5,5),np.uint8)
 
imgGray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY) # greyscale
imgBlur = cv2.GaussianBlur(imgGray,(7,7),0) # blurs before canny to remove artifacts
imgCanny = cv2.Canny(imgBlur,150,200) # finds edges
imgDialation = cv2.dilate(imgCanny,kernel,iterations=1) # thickens edge lines
imgEroded = cv2.erode(imgDialation,kernel,iterations=1) # thins edge lines, does not restore quality if eroding a dialated image
 
cv2.imshow("Gray Image",imgGray)
cv2.imshow("Blur Image",imgBlur)
cv2.imshow("Canny Image",imgCanny)
cv2.imshow("Dialation Image",imgDialation)
cv2.imshow("Eroded Image",imgEroded)
cv2.waitKey(0)