
import numpy as np
import cv2
from google.colab.patches import cv2_imshow
import argparse
from argparse import ArgumentParser
import os
from PIL import Image as im


path = "/content/drive/MyDrive/ImageProcessing/Assignment-28"

parser = ArgumentParser()
parser.add_argument("--encrypted_image", type=str)
parser.add_argument("--key", type=str)
args = parser.parse_args()

encrypted_img = im.open(args.encrypted_image)
encrypted_img = np.array(encrypted_img)

key = np.load(args.key)

decrypted_img = np.zeros_like(encrypted_img)

for i in range(encrypted_img.shape[0]):
    for j in range(encrypted_img.shape[1]):

        key_value = key[i, j]
        new_value = encrypted_img[i, j] - key_value
        
        if new_value < 0:
            new_value = 255 + new_value

        decrypted_img[i, j] = new_value

cv2.imwrite(os.path.join(path + "/output/decrypted_img.jpg"), decrypted_img)
cv2_imshow(decrypted_img)