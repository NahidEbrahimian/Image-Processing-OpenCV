import cv2
import numpy as np
import matplotlib.pyplot as plt

image1 = cv2.imread("/content/drive/MyDrive/Assignment-21/1.jpg")
image2 = cv2.imread("/content/drive/MyDrive/Assignment-21/2.jpg")


image1 = 255 - image1
plt.subplot(1,2,1).imshow(image1)
cv2.imwrite("/content/drive/MyDrive/Assignment-21/Results/01new.jpg", image1)

image2 = 255 - image2
plt.subplot(1,2,2).imshow(image2)
cv2.imwrite("/content/drive/MyDrive/Assignment-21/Results/02new.jpg", image2)

