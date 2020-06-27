# https://tesseract-ocr.github.io/tessdoc/4.0-with-LSTM.html#400-alpha-for-windows
# https://www.youtube.com/watch?v=6DjFscX4I_c&t=63s

# this does not work with fingerontheapp, the numbers that are shown are not recognized by tesseract
# works with other text though, just not the app

import cv2
import numpy as np
import pytesseract

# if you get this error: 
# pytesseract.pytesseract.TesseractError: (1, 'Error opening data file \\Program Files (x86)\\Tesseract-OCR\\eng.traineddata Please make sure the TESSDATA_PREFIX environment variable is set to your "tessdata" directory. Failed loading language \'eng\' Tesseract couldn\'t load any languages! Could not initialize tesseract.')
# search for environmental variables in the start menue and add it to PATH in user variables
pytesseract.pytesseract.tesseract_cmd= "C:/Program Files (x86)/Tesseract-OCR/tesseract.exe"

#img = cv2.imread("pics/numbersletters.png")
#img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB) # converts image from bgr to rgb so tesseract so read it


# use Open Broadcasting Software along with OBS virtual cam to export screencapture of zoom screenshare (from iphone running fingerontheapp) as a virtual webcam
# image bounds taken from 2/3 of a 1080p virtual webcam stream
frameWidth = 1536
frameHeight = 864
cap = cv2.VideoCapture(0)
cap.set(3, 640)
cap.set(4, 480)
cap.set(10, 75)
frameCounter = 0


#detect characters and put boxes around them
def characterDetect (image):
    heightImg, widthImg = image.shape
    boxes = pytesseract.image_to_boxes(image)
    for b in boxes.splitlines():
        b = b.split(" ")
        print(b)
        x, y, w, h = int(b[1]), int(b[2]), int(b[3]), int(b[4])

        cv2.rectangle(img, (x, heightImg - y), (w, heightImg - h), (0,0,255), 2)
        cv2.putText(img,b[0],(x,heightImg - y+30), cv2.FONT_HERSHEY_SIMPLEX, 1, (50,50,255), 2)


while True:
    frameCounter +=1
    if cap.get(cv2.CAP_PROP_FRAME_COUNT) ==frameCounter:
        cap.set(cv2.CAP_PROP_POS_FRAMES,0)
        frameCounter=0
    _, img = cap.read()

    #img = img[260:850,525:1000]
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    imgGray = cv2.cvtColor(img,cv2.COLOR_RGB2GRAY)
    imgBlur = cv2.GaussianBlur(imgGray,(5,5),1)
    imgCanny = cv2.Canny(imgBlur,50,50)
    characterDetect(imgGray)

    cv2.imshow("original", img)
    cv2.imshow("gray", imgGray)
    #cv2.imshow("contour", img)
    if cv2.waitKey(1) and 0xFF == ord('q'):
        break
