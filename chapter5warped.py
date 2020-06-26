import cv2
import numpy as np
 
img = cv2.imread("pics/warped.jpg")
 
width,height = 300,430
pts1 = np.float32([[101,62],[402,15],[209,373],[584,288]]) # corners of image
pts2 = np.float32([[0,0],[width,0],[0,height],[width,height]]) # which corners of the final image pts1 correspond to
matrix = cv2.getPerspectiveTransform(pts1,pts2)
imgOutput = cv2.warpPerspective(img,matrix,(width,height))
 
cv2.imshow("Image",img)
cv2.imshow("Output",imgOutput)
cv2.waitKey(0)