# Script mobile_phone_stream.py enables watching the internet stream from mobile phone or camera. You just have to url in the script where ("YOUR_URL") is written.

import cv2

cap = cv2.VideoCapture('("YOUR_URL")/video')

while(True):
	ret, frame = cap.read()
	cv2.imshow('stream', frame)   
   
	if cv2.waitKey(1) == ord('q'):
		break
		
cap.release()
cv2.destroyAllWindows()
