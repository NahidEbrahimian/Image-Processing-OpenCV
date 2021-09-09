import numpy as np
import matplotlib.pyplot as plt
import cv2

image = cv2.imread("chess pieces.jpg")
image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

image_thresh = cv2.threshold(image_gray, 200, 255, cv2.THRESH_BINARY)[1]
image_thresh = 255 - image_thresh

contours = cv2.findContours(image_thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

if len(contours) == 2:
  contours = contours[0]
else:
  contours = contours[1]

idx = 1

for c in contours:
    x, y, w, h = cv2.boundingRect(c)
    ROI = image[y : y + h, x : x + w]
    cv2.imwrite('/content/drive/MyDrive/ImageProcessing/Assignment-22/Results/Chess_pieces/{}.jpg'.format(idx), ROI)
    idx += 1
