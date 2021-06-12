import numpy as np
import cv2
import matplotlib.pyplot as plt

image4 = cv2.imread("/content/drive/MyDrive/Assignment-21/4.jpg")
image_gry = cv2.cvtColor(image4, cv2.COLOR_RGB2GRAY)

for i in range(image_gry.shape[0]):
  for j in range(image_gry.shape[1]):

    if image_gry[i, j] > 50:
      image_gry[i, j] = 255

plt.imshow(image_gry, cmap='gray')
cv2.imwrite("/content/drive/MyDrive/Assignment-21/Results/04.jpg", image_gry)
