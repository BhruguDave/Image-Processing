#Real Time Face Detection

import cv2,time

video = cv2.VideoCapture(0)

face_cascade = cv2.CascadeClassifier('D:\Image Processing\haarcascade_frontalface_alt.xml')

a = 1

while True:
    a = a + 1
    check, frame = video.read()

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    #cv2.imshow("video frame",gray)

    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.05, minNeighbors=5)

    for x,y,w,h in faces:
        frame = cv2.rectangle(frame, (x,y), (x+w,y+h),(0,255,0),3)

    cv2.imshow("Identified",frame)
    key = cv2.waitKey(2)

    print(frame)

    if key == ord('q'):
        break

print(a)

video.release()

cv2.destroyAllWindows()