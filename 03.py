import numpy as np
import cv2
import matplotlib.pyplot as plt

image3 = cv2.imread("3.jpg")

new_image3 = np.zeros_like(image3)

rows = new_image3.shape[0]
cols = new_image3.shape[1]

for i in range(new_image3.shape[0]):
  for j in range(new_image3.shape[1]):
    
    new_image3[i, j] = image3[rows - 1 - i, cols - 1 - j]

plt.imshow(new_image3, cmap = 'gray')
cv2.imwrite("/content/drive/MyDrive/Assignment-21/Results/03new.jpg", new_image3)

