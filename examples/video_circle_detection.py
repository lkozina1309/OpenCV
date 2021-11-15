import cv2 as cv
import numpy as np
import argparse

cap = cv.VideoCapture('/home/marija/OpenCV/data/Megamind.avi')

while cap.isOpened():
	_, img = cap.read()
	gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
	gray = cv.medianBlur(gray, 5)
	circles = cv.HoughCircles(gray, cv.HOUGH_GRADIENT, 1, 300, param1=20, param2=50, minRadius=0, maxRadius=0)
	if circles is not None:
		circles = np.round(circles[0, :]).astype("int")
		for (x,y,r) in circles:
			cv.circle(img, (x,y), r, (0,255,0), 3)
			cv.circle(img, (x,y), 2, (0,255,255), 3)
	cv.imshow('img', img)
	if cv.waitKey(1) & 0xFF == ord('q'):
		break


cap.release()
