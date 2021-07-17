import cv2
import numpy as np
import matplotlib.pyplot as plt
import os

path = "/content/drive/MyDrive/ImageProcessing/Assignment-22/images/highway"

list_of_images = os.listdir(path)
list_of_images.sort()

images = []

for i in range(len(list_of_images)):

  image = cv2.imread(os.path.join(path, f'{list_of_images[i]}'))
  image = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
  images.append(image)

highway_img = np.zeros_like(images[0])

for i in range(len(images)):
  highway_img = highway_img + images[i] // len(images)

plt.imshow(highway_img, cmap = 'gray')

path = "/content/drive/MyDrive/ImageProcessing/Assignment-22/Results"
cv2.imwrite(os.path.join(path, "highway_img.jpg"), highway_img)