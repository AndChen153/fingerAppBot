import cv2
 
img = cv2.imread("pics/picture.PNG")
print(img.shape) # prints size of image
 
imgResize = cv2.resize(img,(1000,200)) # width,height
print(imgResize.shape)
 
imgCropped = img[0:200,0:500] # height:width, (height value 0 starts at the top)
 
cv2.imshow("Image",img)
cv2.imshow("Image Resize",imgResize)
cv2.imshow("Image Cropped",imgCropped)
 
cv2.waitKey(0)