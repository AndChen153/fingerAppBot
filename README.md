# opencvtutorial
This is my attempt to cheat the Mr. Beast FingerOnTheApp challenge by attaching a touch pen onto my chessboard. I tried finding contours, using the tesseract library, and finally decided on using Haar Cascade deep learning.
opencv tutorial https://www.youtube.com/watch?v=WQeoO7MI0Bs

### Haar Cascade
This was the most sucessful method and it detected the "move finger here" buttons close to 100% of the time. It is also able to detect more than one thing at a time, which will be much more useful than just detecting one thing at a time.

### Tesseract
python library for detecting numbers, did not work in my use case. the number in the middle of the app just wasnt recognized

### Contours
Contours can only work for one thing at a time and this was not good enough because of this tweet by Mr. Beast: https://twitter.com/MrBeastYT/status/1275490794577641472 .
