# Script my_face_detection.py uses webcam to detect face i draw blue rectangle around it. 
# It uses classifier haar_cascades.xml so You need to have it and write exact path to it.

import cv2
import numpy as np

cap = cv2.VideoCapture(0)
face_cascade = cv2.CascadeClassifier('haar_cascades.xml')

while(True):
	ret, frame = cap.read()
	gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
	faces = face_cascade.detectMultiScale(gray, 1.1, 4)
	
	
	
	for (x, y , w ,h) in faces:
		cv2.rectangle(frame, (x,y), (x+w, y+h), (255, 0 , 0), 3)
	cv2.imshow('frame', frame)	
	if cv2.waitKey(1) & 0xFF == ord('q'):
		break
		
cap.release()
cv2.destroyAllWindows()
