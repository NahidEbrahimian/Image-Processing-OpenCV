import numpy as np
import cv2
import matplotlib.pyplot as plt
import os

img_a = cv2.imread("a.tif")
img_b = cv2.imread("b.tif")

img_a = cv2.cvtColor(img_a, cv2.COLOR_RGB2GRAY)
img_b = cv2.cvtColor(img_b, cv2.COLOR_RGB2GRAY)
img_a = 255 - img_a

img_pass = cv2.multiply(img_a, img_b)
img_pass = 255 - img_pass

plt.imshow(img_pass, cmap = 'gray')

path = "/content/drive/MyDrive/ImageProcessing/Assignment-22/Results"
cv2.imwrite(os.path.join(path, "img_pass.jpg"), img_pass)