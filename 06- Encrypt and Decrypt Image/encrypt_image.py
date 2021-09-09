

import numpy as np
import cv2
from google.colab.patches import cv2_imshow
import argparse
from argparse import ArgumentParser
import os
from PIL import Image as im


path = "/content/drive/MyDrive/ImageProcessing/Assignment-28"

parser = ArgumentParser()
parser.add_argument("--input_image", type=str)
args = parser.parse_args()

img = cv2.imread(args.input_image)
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# cv2_imshow(img)

key = np.random.randint(0, pow(2, 8)-1, size = (img.shape[0], img.shape[1]), dtype=int)
np.save(os.path.join(path+ "/output/key"), key)

encrypted_img = np.zeros_like(img)

for i in range(img.shape[0]):
    for j in range(img.shape[1]):

        key_value = key[i, j]
        new_value = img[i, j] + key_value
        if new_value > 255:
            new_value = new_value - 255

        encrypted_img[i, j] = new_value

# cv2_imshow(encrypted_img)

encrypted_img = im.fromarray(encrypted_img)
encrypted_img.save(os.path.join(path+ "/output/encrypted_img.bmp"))
