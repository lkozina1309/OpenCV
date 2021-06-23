# Script gradient.py shows gradients in an image. It uses image of a footballer Mason Mount so You need to download an image and provide the correct path to it.

import numpy as np
import cv2
from matplotlib import pyplot as plt

img = cv2.imread('mount.jpeg', cv2.IMREAD_GRAYSCALE)

titles = ['image']
images = [img]
for i in range(1):
	plt.subplot(1,1,i+1), plt.imshow(images[i], 'gray')
	plt.title(titles[i])
	plt.xticks([]), plt.yticks([])
	
plt.show()
