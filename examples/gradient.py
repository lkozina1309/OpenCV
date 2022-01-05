import cv2

img = cv2.imread('/home/marija/OpenCV/data/water_balloons.jpg')

lap = cv2.Laplacian(img, cv2.CV_64F, ksize=3)

cv2.imshow('Laplacian', lap)

cv2.waitKey(0)
cv2.destroyAllWindows()
