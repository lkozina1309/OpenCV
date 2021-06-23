# Script region_of_interest.py shows image of footballer Mason Mount and copy of the ball.
# To use script on some other image, you need to know the location of your region of interest (the ball in my example).
# Script mouse_click.py can be used for that purpose.


import numpy as np
import cv2

img = cv2.imread('/home/marija/opencv/samples/data/mount.jpeg', 1)

img = cv2.resize(img, (512,512))

ball = img[430:508, 109:170]
img[430:508, 380:441] = ball



cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
