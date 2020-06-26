import cv2

img = cv2.imread("pics/picture.PNG")

cv2.imshow("picture",img) # shows picture
cv2.waitKey(0) # 0 is leave open for infinite time, other values in ms