import cv2 
from PIL import Image
import pytesseract


def car_rec(image):
    text = pytesseract.image_to_string(image)
    return text

img = cv2.imread("text.jpeg")

#img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
#img = cv2.threshold(img, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]
#img = cv2.medianBlur(img, 5)

print(car_rec(img))

