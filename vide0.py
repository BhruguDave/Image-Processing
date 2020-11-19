import cv2

video = cv2.VideoCapture(0)

face_cascade = cv2.CascadeClassifier('D:\Hackathon\haarcascade_frontalface_alt.xml')

check, frame = video.read()

gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

faces = face_cascade.detectMultiScale(gray, scaleFactor=1.05, minNeighbors=5)

for x,y,w,h in faces:
    frame = cv2.rectangle(frame, (x,y), (x+w,y+h), (0,255,0), 3)

cv2.imshow("framee",frame)

cv2.waitKey(0)

video.release()

cv2.destroyAllWindows()