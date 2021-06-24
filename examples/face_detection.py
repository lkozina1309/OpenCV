# Script face_detection.py detects faces in an animated video Megamind.avi and classifier haar_cascades.xml, so You need to download these scripts and provide the correct path. 

import cv2

face_cascade = cv2.CascadeClassifier('haar_cascades.xml')

cap = cv2.VideoCapture('Megamind.avi')

while cap.isOpened():
    _, img = cap.read()

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.1, 4)

    for (x, y , w ,h) in faces:
        cv2.rectangle(img, (x,y), (x+w, y+h), (255, 0 , 0), 3)

    
    cv2.imshow('img', img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
