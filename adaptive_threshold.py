# Script adaptive_threshold.py shows methods of thresholding. It uses image sudoku.png so You need to downoad it and provide the right path to it.


import numpy as np
import cv2 as cv

img = cv.imread('/home/marija/opencv/samples/data/sudoku.png', 0)
#_th1 = cv.treshold(img, 127, 255, cv.THRESH_BINARY)
th2 = cv.adaptiveThreshold(img, 255, cv.ADAPTIVE_THRESH_MEAN_C, cv.THRESH_BINARY, 11, 2);
th3 = cv.adaptiveThreshold(img, 255, cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY, 11, 2);

cv.imshow("Image", img)
cv.imshow("Th2", th2)
cv.imshow("Th3", th3)

cv.waitKey(0)
cv.destroyAllWindows()
