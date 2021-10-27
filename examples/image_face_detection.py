import cv2

face_cascade = cv2.CascadeClassifier('haar_cascades.xml')
img = cv2.imread('chelsea.jpeg')
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
faces = face_cascade.detectMultiScale(img, 1.1, 4)

for (x, y , w ,h) in faces:
	cv2.rectangle(img, (x,y), (x+w, y+h), (255, 0 , 0), 3)
	
cv2.imshow('img', img)

cv2.waitKey(0)
cv2.destroyAllWindows()

