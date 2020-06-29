# using cascade trainer gui to generate the cascade files
# https://amin-ahmadi.com/cascade-trainer-gui/  (download at bottom of page)
# https://www.youtube.com/watch?v=dZ4itBvIjVY
# https://www.murtazahassan.com/custom-object-detection/

# use Open Broadcasting Software along with OBS virtual cam to export screencapture of zoom screenshare (from iphone running fingerontheapp) as a virtual webcam
# https://obsproject.com/forum/resources/obs-virtualcam.949/
# image bounds taken from 2/3 of a 1080p virtual webcam stream

# keyboard for typing https://pypi.org/project/keyboard/

# useful links for encoutered bugs:
# https://amin-ahmadi.com/2017/07/26/how-to-get-past-the-infamous-insufficient-count-of-samples-error-in-opencv-cascade-training/

# if you get an error saying that cascade can't rename a photo move the folder containing all positive and negative images to desktop and keep trying until it fully renames all images

import cv2
import math
import keyboard
import time
import statistics 

################################################################
path = 'haarcascades/fingerappcascadeV2.xml'  # cascade path, V2 works the best
cameraNo = 0                       # camera number
objectName = 'Move Finger Here'       # bounding box label
frameWidth= 1536                     # display width
frameHeight = 864                  # display height
color= (0,255,255)                 # color space in BGR
#################################################################
 
cap = cv2.VideoCapture(cameraNo)
cap.set(3, frameWidth)
cap.set(4, frameHeight)

iterable = 60
strs = "SEND"
 
def empty(a):
    pass

def roundup(x):
    return int(math.ceil(x / 10.0)) * 10

def sendData(x, y):
    keyboard.write(str(x) + " " + str(y))
    keyboard.send("enter")

def compare(first, second):
    comp = abs(first-second)
    if comp > 40:
        return True
    else:
        return False
 
# create the trackbar
cv2.namedWindow("Result")
cv2.resizeWindow("Result",frameWidth,frameHeight+100)
cv2.createTrackbar("Scale","Result",7,1000,empty)
cv2.createTrackbar("Neig","Result",30,50,empty)
cv2.createTrackbar("Min Area","Result",20700,100000,empty)
cv2.createTrackbar("Brightness","Result",180,255,empty)
# 7 30 24700 180
 
# Load the classifier
cascade = cv2.CascadeClassifier(path)
 
while True:
    # set camera brightness
    cameraBrightness = cv2.getTrackbarPos("Brightness", "Result")
    cap.set(10, cameraBrightness)

    # Get image from camera and convert to greyscale
    success, img = cap.read()
    img = img[305:830,505:1035] # height:width, (height value 0 starts at the top)220 120220 120
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
            cv2.rectangle(img,(moveToX-2,moveToY-2),(moveToX+2,moveToY+2),color,3)


            if iterable > 50:
                sendData(moveToX, moveToY)
                print(moveToX, moveToY)
                iterable = 0
        
    iterable += 1
    #print(iterable)
            


    
 
    cv2.imshow("Result", img)
    if cv2.waitKey(1) and 0xFF == ord('q'): # waits until q is pressed to quit
        break