import numpy as np
import time
import cv2
import os

img = cv2.imread('/home/marija/OpenCV/data/traffic.jpeg')
img = cv2.resize(img, (1500,800))
useCuda = True

with open('/home/marija/OpenCV/dnn/model/object_detection_classes_coco.txt', 'r') as f:
	classes = f.read().splitlines()

net = cv2.dnn.readNetFromDarknet('/home/marija/OpenCV/dnn/model/yolov4.cfg', '/home/marija/OpenCV/dnn/model/yolov4.weights')
model = cv2.dnn_DetectionModel(net)
model.setInputParams(scale=1 / 255, size=(416, 416), swapRB=True)
if useCuda:
	net.setPreferableBackend(cv2.dnn.DNN_BACKEND_CUDA)
	net.setPreferableTarget(cv2.dnn.DNN_TARGET_CUDA)

classIds, scores, boxes = model.detect(img, confThreshold=0.6, nmsThreshold=0.4)

for (classId, score, box) in zip(classIds, scores, boxes):
	cv2.rectangle(img, (box[0], box[1]), (box[0] + box[2], box[1] + box[3]), color=(0, 255, 0), thickness=2)
	text = '%s: %.2f' % (classes[classId[0]], score)
	cv2.putText(img, text, (box[0], box[1] - 5), cv2.FONT_HERSHEY_SIMPLEX, 1, color=(0, 255, 0), thickness=2)
	
cv2.imshow('Image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()


	
	
