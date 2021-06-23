# Script road_line_detection_video.py detect lines on the road we need to drive. 
# It uses video road_lines.avi so You need to download it and provide the correct path to it.


import numpy as np
import cv2
import matplotlib.pylab as plt

def region(img, vertices):
	mask = np.zeros_like(img)
	#channel_count = img.shape[2]
	match_mask_color = 255
	cv2.fillPoly(mask,vertices, match_mask_color)
	masked_image = cv2.bitwise_and(img, mask)
	return masked_image
	
def drawLines(img, lines):
	img = np.copy(img)
	blank_image = np.zeros((img.shape[0], img.shape[1], 3), dtype=np.uint8)
	for line in lines:
		for x1,y1,x2,y2 in line:
			cv2.line(blank_image, (x1,y1), (x2,y2), (0,255,0), thickness=5)
		
	img = cv2.addWeighted(img, 0.8, blank_image, 1, 0.0)
	return img

def process(image):
	
	height = image.shape[0]
	width = image.shape[1]

	roi = [
		(width/3, height),
		(width/3, 0),
		(width, 0)
	]	
	
	gray_image = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
	canny_image = cv2.Canny(gray_image, 100, 120)	
	mask_image = region(canny_image, np.array([roi], np.int32)) 
	lines = cv2. HoughLinesP(mask_image, rho=2, theta=np.pi/60, threshold=170, lines=np.array([]), minLineLength=50,maxLineGap=100)

	image_with_lines = drawLines(image, lines)
	return image_with_lines
	
cap = cv2.VideoCapture('road_lines.avi')

while(cap.isOpened()):
	ret, frame = cap.read()
	frame = process(frame)
	cv2.imshow('frame',frame)
	if cv2.waitKey(1) & 0xFF == ord('q'):
		break

cap.release()
cv2.destroyAllWindows()
