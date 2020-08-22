# FingerApp Bot
Mr Beast announced his challenge a week before it started and I learned how to use opencv and wrote all of this code within 7 days so I know it is kind of sloppy.

This is my attempt make a bot to beat the Mr. Beast FingerOnTheApp challenge by attaching a touchscreen stylus onto my automated chessboard. The code used to move the pen arround is located in https://github.com/AndChen153/ChessBoard/tree/master/fingerontheapp. I ssh'd into the raspberry pi and inputed the positioning data of the buttons to press using the python library keyboard. I felt that this was the quicker way to transmit the data versus creating a server with the raspberry pi and my laptop.

I tried finding contours, using the tesseract library, and finally decided on using Haar Cascade deep learning after following this opencv tutorial: https://www.youtube.com/watch?v=WQeoO7MI0Bs.

### Results
Video of my project working in the practice mode of the app with a side by side view of the phone and the laptop screen (This was not the finished version I forgot to take video of the finished version before the challenge started-the practice mode closed after the challenge started): https://www.youtube.com/watch?v=xRqSazZKHoc&feature=youtu.be

Extended video of just the phone: https://www.youtube.com/watch?v=EAtvmaOwU-I&feature=youtu.be

Extended video of Haar Cascade program with a screen recording of me playing the app: https://www.youtube.com/watch?v=kAcWppZJqxM&feature=youtu.be

Unfortunately I was kicked as soon as the challenge started because of two possible reasons. Before the start of the challenge I was still testing my program in the practice mode, and the app removed me from practice mode and placed me into a waiting room for the actual challenge to start. During the transition into the waiting room I did not remove the pen and put it back on for the app to detect a new touch so the app may not have thought I was "touching" the screen. Another possible reason was that Mr. Beast's bot detection method was to look at the time spent in the practice mode and the movemen patterns during that time. I spent 10-15 hours in the practice mode testing my program and that probably raised a red flag and caused my removal from the challenge.

### Contours
Contours would usually only work for one thing at a time and this was not good enough because of a tweet from Mr beast saying that the app would be updated to prevent people from making bots. I interpreted this as him adding a "do not press" button or something similar to that.

### Tesseract
Prebuilt Python library for detecting numbers, worked very well on text with a solid background, but did not work in my use case. The number in the middle of the button to press wasn't recognized.

### Haar Cascade
This was the most sucessful method and it detected the "move finger here" buttons close to 100% of the time. It is also able to detect more than one thing at a time, which would allow me to identify the bot prevention methods if implemented in the way I predicted.

