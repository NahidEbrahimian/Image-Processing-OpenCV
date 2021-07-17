import numpy as np
import matplotlib.pyplot as plt
import cv2

img = cv2.imread("Mona_Lisa.jpg")
img = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)

def get_gradient_2d(start, stop, width, height):
    return np.tile(np.linspace(start, stop, width), (height, 1))

gradient_img = get_gradient_2d(10, 250, img.shape[1], img.shape[0])
gradient_img = np.uint8(gradient_img)

Mona_Lisa = (img/gradient_img) * 255

plt.imshow(Mona_Lisa, cmap = 'gray')
cv2.imwrite("/content/drive/MyDrive/ImageProcessing/Assignment-22/Results/Mona_Lisa.jpg", Mona_Lisa)