# Script mobile_phone_stream.py enables watching the internet stream from mobile phone or camera. You just have to url in the script where ("YOUR_URL") is written.

import cv2
from mtcnn.mtcnn import MTCNN

cap = cv2.VideoCapture('C:/Users/38595/Desktop/OpenCV/data/Megamind.avi')

while cap.isOpened():
	_, img = cap.read()
	img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
	detector = MTCNN()
	faces = detector.detect_faces(img)
	
	for i in range (len(faces)):
		x1, y1, width, height = faces[i]['box']
		x2, y2 = x1 + width, y1 + height
		cv2.rectangle(img, (x1, y1), (x2, y2), (0, 0, 255), 2)
		
	cv2.imshow('img', img)
	if cv2.waitKey(1) & 0xFF == ord('q'):
		break
		
cap.release()
