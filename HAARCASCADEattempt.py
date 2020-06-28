# using cascade trainer gui to generate the cascade files
# https://amin-ahmadi.com/cascade-trainer-gui/  (download at bottom of page)
# https://www.youtube.com/watch?v=dZ4itBvIjVY

# use Open Broadcasting Software along with OBS virtual cam to export screencapture of zoom screenshare (from iphone running fingerontheapp) as a virtual webcam
# image bounds taken from 2/3 of a 1080p virtual webcam stream

# keyboard for typing https://pypi.org/project/keyboard/

# useful links for encoutered bugs:
# https://amin-ahmadi.com/2017/07/26/how-to-get-past-the-infamous-insufficient-count-of-samples-error-in-opencv-cascade-training/

# if you get an error saying that cascade can't rename a photo move the folder containing all positive and negative images to desktop

import cv2
import math
import keyboard
import time

################################################################
path = 'haarcascades/fingerappcascade.xml'  # cascade path
cameraNo = 0                       # camera number
objectName = 'Move Finger Here'       # bounding box label
frameWidth= 1536                     # display width
frameHeight = 864                  # display height
color= (0,255,255)                 # color space in BGR
#################################################################
 
 
cap = cv2.VideoCapture(cameraNo)
cap.set(3, frameWidth)
cap.set(4, frameHeight)
 
def empty(a):
    pass

def roundup(x):
    return int(math.ceil(x / 10.0)) * 10

def sendData():
    keyboard.write(str(moveToX) + " " + str(moveToY))
    keyboard.send("enter")
 
# create the trackbar
cv2.namedWindow("Result")
cv2.resizeWindow("Result",frameWidth,frameHeight+100)
cv2.createTrackbar("Scale","Result",5,1000,empty)
cv2.createTrackbar("Neig","Result",8,50,empty)
cv2.createTrackbar("Min Area","Result",20700,100000,empty)
cv2.createTrackbar("Brightness","Result",180,255,empty)
# 5 10 20700 180
 
# Load the classifier
cascade = cv2.CascadeClassifier(path)
 
while True:
    # set camera brightness
    cameraBrightness = cv2.getTrackbarPos("Brightness", "Result")
    cap.set(10, cameraBrightness)

    # Get image from camera and convert to greyscale
    success, img = cap.read()
    img = img[305:830,555:985] # height:width, (height value 0 starts at the top)220 120220 120
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Detect the objects
    scaleVal =1 + (cv2.getTrackbarPos("Scale", "Result") /1000)
    neig=cv2.getTrackbarPos("Neig", "Result")
    objects = cascade.detectMultiScale(gray,scaleVal, neig)

    # Display bounding boxes around detected objects
    for (x,y,w,h) in objects:
        area = w*h
        minArea = cv2.getTrackbarPos("Min Area", "Result")
        if area >minArea:
            cv2.rectangle(img,(x,y),(x+w,y+h),color,3)
            cv2.putText(img,objectName,(x,y-5),cv2.FONT_HERSHEY_COMPLEX_SMALL,1,color,2)
            roi_color = img[y:y+h, x:x+w]
            moveToX,moveToY = (roundup(x+w/2),roundup(y+h/2))
            sendData()
            time.sleep(3)

    
 
    cv2.imshow("Result", img)
    if cv2.waitKey(1) and 0xFF == ord('q'): # waits until q is pressed to quit
        break