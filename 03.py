import numpy as np
import cv2
import matplotlib.pyplot as plt

image3 = cv2.imread("/content/drive/MyDrive/Assignment-21/3.jpg")

image3 = cv2.rotate(image3, cv2.ROTATE_180)
plt.imshow(image3)
cv2.imwrite("/content/drive/MyDrive/Assignment-21/Results/03new.jpg", image3)
