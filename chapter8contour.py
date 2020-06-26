import cv2
import numpy as np 


frameWidth = 1536
frameHeight = 864
cap = cv2.VideoCapture(1)
cap.set(3, frameWidth)
cap.set(4, frameHeight)
cap.set(10, 75)
frameCounter = 0

def contour(image):
    contours,hierarchy = cv2.findContours(image,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)
    for cnt in contours:
        area = cv2.contourArea(cnt)
        #print (area)
        if area>700 and area<900:
            cv2.drawContours(img, cnt, -1, (0, 0, 0), 2)
            peri = cv2.arcLength(cnt,False)
            #print(peri)
            approx = cv2.approxPolyDP(cnt,0.02*peri,True)
            #print(len(approx))
            objCor = len(approx)
            x, y, w, h = cv2.boundingRect(approx)
            aspRatio = w/float(h)
            #and aspRatio < 0.98 and aspRatio >1.03
            if objCor > 5:
                #print (x,y)
                cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)
                cv2.putText(img,"number",
                        (x+(w//2)-10,y+(h//2)-10),cv2.FONT_HERSHEY_COMPLEX,0.7,
                        (0,0,0),2)




'''path = "pics/picture.PNG"
img = cv2.imread(path)
img = cv2.resize(img,(506,900))
img = img[283:900,0:506]
imgContour = img.copy()

print(img.shape)
imgGray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
imgBlur = cv2.GaussianBlur(imgGray,(5,5),1)
imgCanny = cv2.Canny(imgBlur,490,270)
contour(imgCanny)

#cv2.imshow("original", img)
cv2.imshow("canny", imgCanny)
cv2.imshow("contour", imgContour)
cv2.waitKey(0)'''

while True:
    frameCounter +=1
    if cap.get(cv2.CAP_PROP_FRAME_COUNT) ==frameCounter:
        cap.set(cv2.CAP_PROP_POS_FRAMES,0)
        frameCounter=0
    _, img = cap.read()

    img = img[260:850,525:1000]

    #imgContour = img.copy()
    imgGray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    imgBlur = cv2.GaussianBlur(imgGray,(5,5),1)
    imgCanny = cv2.Canny(imgBlur,50,50)
    contour(imgCanny)

    #cv2.imshow("original", img)
    cv2.imshow("canny", imgCanny)
    cv2.imshow("contour", img)
    if cv2.waitKey(1) and 0xFF == ord('q'):
        break


cap.release()
cv2.destroyAllWindows()
