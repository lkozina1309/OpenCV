import cv2

img = cv2.imread('mount.jpeg')
img = cv2.resize(img, (1000,1000))

lap = cv2.Laplacian(img, cv2.CV_64F, ksize=3)
sobelX = cv2.Sobel(img, cv2.CV_64F, 1, 0)
sobelY = cv2.Sobel(img, cv2.CV_64F, 0, 1)
sobelCombined = cv2.bitwise_or(sobelX, sobelY)

cv2.imshow('Laplacian', lap)
cv2.imshow('sobelX', sobelX)
cv2.imshow('sobelY', sobelY)
cv2.imshow('sobelCombined', sobelCombined)


cv2.waitKey(0)
cv2.destroyAllWindows()
