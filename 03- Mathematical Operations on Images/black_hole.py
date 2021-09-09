import numpy as np
import cv2
import matplotlib.pyplot as plt
import os

path = "/content/drive/MyDrive/ImageProcessing/Assignment-22/images/black hole"


list_of_patches = os.listdir(path)
list_of_patches.sort()
images_without_noise = []


for i in range(len(list_of_patches)):

    images = []
    list_of_images = os.listdir(os.path.join(path, list_of_patches[i]))
    list_of_images.sort()


    for j in range(len(list_of_images)):

        image = cv2.imread(os.path.join(path,f'{list_of_patches[i]}' ,f'{list_of_images[j]}'))
        image = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
        images.append(image)

    image_without_noise = np.zeros_like(images[0])

    for k in range(len(images)):
        image_without_noise = image_without_noise + images[k] // len(list_of_images)

    images_without_noise.append(image_without_noise)


h = images[0].shape[0] * 2
w = images[0].shape[1] * 2

black_hole = np.zeros((h, w), dtype = 'uint8')

h_block_size = h // 2
w_block_size = w // 2
n = 0

for i in range(0, h, h_block_size):
  for j in range(0, w, w_block_size):

      black_hole[i : i + h_block_size, j: j + w_block_size] = images_without_noise[n]
      n = n + 1

plt.imshow(image_finall, cmap = 'gray')

path = "/content/drive/MyDrive/ImageProcessing/Assignment-22/Results"
cv2.imwrite(os.path.join(path, "black_hole.jpg"), black_hole)