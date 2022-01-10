import numpy as np
import cv2 as cv

cap = cv.VideoCapture('vtest.avi')
#bg_sub = cv.bgsegm.createBackgroundSubtractorMOG()
#bg_sub  = cv.createBackgroundSubtractorMOG2(detectShadows=True)
bg_sub = cv.createBackgroundSubtractorKNN(detectShadows=True)

while True:
    ret, frame = cap.read()
    if frame is None:
        break
    img = bg_sub.apply(frame)
    cv.imshow('Background subtraction', img)

    keyboard = cv.waitKey(30)
    if keyboard == 'q' or keyboard == 27:
        break
cap.release()
cv.destroyAllWindows()
