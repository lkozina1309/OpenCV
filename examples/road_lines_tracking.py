# Script road_lines_tracking.py uses HoughLinesP to detect the lines and masking to image and then specifies the region of interest to track only lines we are interested in.
# Script uses an image road.jpg so You to download it and provide the correct path to it.


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
	blank_image = np.zeros((img.shape[0], img.shape[1], 3), dtype=np.uint8)
	for line in lines:
		for x1,y1,x2,y2 in line:
			cv2.line(blank_image, (x1,y1), (x2,y2), (0,255,0), thickness=3)
		
	img = cv2.addWeighted(img, 0.8, blank_image, 1, 0.0)
	return img

def drawLines(img, lines):
	img = np.copy(img)
	blank_image = np.zeros((img.shape[0], img.shape[1], 3), dtype=np.uint8)
	for line in lines:
		for x1,y1,x2,y2 in line:
			cv2.line(blank_image, (x1,y1), (x2,y2), (0,255,0), thickness=5)
		
	img = cv2.addWeighted(img, 0.8, blank_image, 1, 0.0)
	return img

image = cv2.imread('/home/marija/OpenCV/data/road.jpg')

image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

height = image.shape[0]
width = image.shape[1]

roi = [
	(width/2, height),
	(width/2, height/2),
	(width, height*2/3)
]

gray_image = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
canny_image = cv2.Canny(gray_image, 100, 200)	
mask_image = region(canny_image, np.array([roi], np.int32)) 
lines = cv2. HoughLinesP(mask_image, rho=6, theta=np.pi/60, threshold=160, lines=np.array([]), minLineLength=40,maxLineGap=25)

image_with_lines = drawLines(image, lines)
plt.imshow(image_with_lines)
plt.show()
