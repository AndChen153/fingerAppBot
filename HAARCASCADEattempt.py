# using cascade trainer gui to generate the cascade files
# https://pypi.org/project/opencv-python/ opencv install
# https://amin-ahmadi.com/cascade-trainer-gui/  (download at bottom of page)
# https://www.youtube.com/watch?v=dZ4itBvIjVY tutorial
# https://www.murtazahassan.com/custom-object-detection/

# use Open Broadcasting Software along with OBS virtual cam to export screencapture of zoom screenshare (from iphone running fingerontheapp) as a virtual webcam
# https://obsproject.com/forum/resources/obs-virtualcam.949/
# image bounds taken from 2/3 of a 1080p virtual webcam stream

# keyboard spoofer for typing https://pypi.org/project/keyboard/

# useful links for encoutered bugs:
# https://amin-ahmadi.com/2017/07/26/how-to-get-past-the-infamous-insufficient-count-of-samples-error-in-opencv-cascade-training/

# if you get an error saying that cascade can't rename a photo move the folder containing all positive and negative images to desktop and keep trying until it fully renames all images

import cv2
import math
import keyboard
import time
from PIL import ImageGrab
import numpy as np

################################################################
path = 'haarcascades/fingerappcascadeV2.xml'  # cascade path, V2 works the best
path2 = 'haarcascades/fingerappcascadeV2.xml'  # cascade path, V2 works the best
cameraNo = 0                      # camera number
objectName = 'Move Finger Here'       # bounding box label
frameWidth= 1536                     # display width
frameHeight = 864                  # display height
color= (0,255,255)                 # color space in BGR
color2= (0,0,255) 
#################################################################
 
#cap = cv2.VideoCapture(cameraNo)
#cap.set(3, frameWidth)
#cap.set(4, frameHeight)


# four character code object for video writer
fourcc = cv2.VideoWriter_fourcc(*'XVID')
# video writer object
out = cv2.VideoWriter("output.avi", fourcc, 5.0, (1366, 768))

iterable = 60
frameCount = 20 # how many frames between detections, needs to be lower on lower spec machines with higher resolutions
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
'''cv2.namedWindow("Result")
cv2.resizeWindow("Result",frameWidth,frameHeight+100)
cv2.createTrackbar("Scale","Result",7,1000,empty)
cv2.createTrackbar("Neig","Result",30,50,empty)
cv2.createTrackbar("Min Area","Result",20700,100000,empty)
cv2.createTrackbar("Brightness","Result",180,255,empty)'''
# 7 30 24700 180
 
# Load the classifier
cascade = cv2.CascadeClassifier(path)
cascade1 = cv2.CascadeClassifier(path2)

while True:
    # set camera brightness
    #cameraBrightness = cv2.getTrackbarPos("Brightness", "Result")
    #cap.set(10, cameraBrightness)

    # Get image from camera and convert to greyscale
    img = ImageGrab.grab()
    img = np.array(img)
    #success, img = cap.read()
    #img = img[273:835,505:1035] # height:width, (height value 0 starts at the top)
    img = img[360:1080,640:1280] # height:width, (height value 0 starts at the top)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    #img = cv2.resize(img,(265,265)) # width,height
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Detect the objects
    #scaleVal =1 + (cv2.getTrackbarPos("Scale", "Result") /1000)
    #neig=cv2.getTrackbarPos("Neig", "Result")
    scaleVal =1 + (7/1000)
    neig=30
    objects = cascade.detectMultiScale(gray,scaleVal, neig)

    scaleVal1 =1 + (7/1000)
    neig1=30
    objects1 = cascade1.detectMultiScale(gray,scaleVal1, neig1)

    # Display bounding boxes around detected objects
    for (x,y,w,h) in objects:
        area = w*h
        #minArea = cv2.getTrackbarPos("Min Area", "Result")
        #if area >minArea:
        if area >20700:
            cv2.rectangle(img,(x,y),(x+w,y+h),color,3)
            cv2.putText(img,objectName,(x,y-5),cv2.FONT_HERSHEY_COMPLEX_SMALL,1,color,2)
            roi_color = img[y:y+h, x:x+w]
            moveToX,moveToY = (roundup(x+w/2),roundup(y+h/2))
            #cv2.rectangle(img,(moveToX-2,moveToY-2),(moveToX+2,moveToY+2),color,3)

            
            if iterable > frameCount:
                sendData(moveToX, moveToY)
                print(moveToX, moveToY)
                iterable = 0
    
    for (x,y,w,h) in objects1:
        area = w*h
        #minArea = cv2.getTrackbarPos("Min Area", "Result")
        #if area >minArea:
        if area >20700:
            cv2.rectangle(img,(x,y),(x+w,y+h),color2,3)
            cv2.putText(img,objectName,(x,y-5),cv2.FONT_HERSHEY_COMPLEX_SMALL,1,color2,2)
            roi_color = img[y:y+h, x:x+w]
            moveToX,moveToY = (roundup(x+w/2),roundup(y+h/2))
            cv2.rectangle(img,(moveToX-2,moveToY-2),(moveToX+2,moveToY+2),color2,3)

            
            if iterable > frameCount:
                sendData(moveToX, moveToY)
                print(moveToX, moveToY)
                iterable = 0

    iterable += 1
    #print(iterable)
            


    
 
    cv2.imshow("Result", img)
    #cv2.imshow("Result", gray)
    if cv2.waitKey(1) and 0xFF == ord('q'): # waits until q is pressed to quit
        break