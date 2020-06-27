# using cascade trainer gui to generate the cascade files
# https://amin-ahmadi.com/cascade-trainer-gui/  (download at bottom of page)
# https://www.youtube.com/watch?v=dZ4itBvIjVY

# if you get an error saying that cascade can't rename a photo move the folder containing all positive and negative images to desktop

import cv2
 
################################################################
path = 'haarcascades/cascade.xml'  # PATH OF THE CASCADE
cameraNo = 1                       # CAMERA NUMBER
objectName = 'Finger'       # OBJECT NAME TO DISPLAY
frameWidth= 1536                     # DISPLAY WIDTH
frameHeight = 864                  # DISPLAY HEIGHT
color= (255,0,255)
#################################################################
 
 
cap = cv2.VideoCapture(cameraNo)
cap.set(3, frameWidth)
cap.set(4, frameHeight)
 
def empty(a):
    pass
 
# CREATE TRACKBAR
cv2.namedWindow("Result")
cv2.resizeWindow("Result",frameWidth,frameHeight+100)
cv2.createTrackbar("Scale","Result",400,1000,empty)
cv2.createTrackbar("Neig","Result",8,50,empty)
cv2.createTrackbar("Min Area","Result",0,100000,empty)
cv2.createTrackbar("Brightness","Result",180,255,empty)
 
# LOAD THE CLASSIFIERS DOWNLOADED
cascade = cv2.CascadeClassifier(path)
 
while True:
    # SET CAMERA BRIGHTNESS FROM TRACKBAR VALUE
    cameraBrightness = cv2.getTrackbarPos("Brightness", "Result")
    cap.set(10, cameraBrightness)
    # GET CAMERA IMAGE AND CONVERT TO GRAYSCALE
    success, img = cap.read()
    img = img[260:850,525:1000]
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # DETECT THE OBJECT USING THE CASCADE
    scaleVal =1 + (cv2.getTrackbarPos("Scale", "Result") /1000)
    neig=cv2.getTrackbarPos("Neig", "Result")
    objects = cascade.detectMultiScale(gray,scaleVal, neig)
    # DISPLAY THE DETECTED OBJECTS
    for (x,y,w,h) in objects:
        area = w*h
        minArea = cv2.getTrackbarPos("Min Area", "Result")
        if area >minArea:
            cv2.rectangle(img,(x,y),(x+w,y+h),color,3)
            cv2.putText(img,objectName,(x,y-5),cv2.FONT_HERSHEY_COMPLEX_SMALL,1,color,2)
            roi_color = img[y:y+h, x:x+w]
 
    cv2.imshow("Result", img)
    if cv2.waitKey(1) and 0xFF == ord('q'): # waits until q is pressed to quit
        break