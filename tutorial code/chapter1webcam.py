import cv2
stream = cv2.VideoCapture(0)
stream.set(3, 640) # wdith
stream.set(4, 480) # height
stream.set(10,150) # brightness

while True:
    success, img = stream.read() # sets success to true/false depending on if the stream is opened correctly
    img = cv2.Canny(img, 200,200)
    cv2.imshow("Result", img)
    if cv2.waitKey(1) and 0xFF == ord('q'): # waits until q is pressed to quit
        break