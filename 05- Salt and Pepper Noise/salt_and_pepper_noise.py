
import cv2
import numpy as np
from google.colab.patches import cv2_imshow
import argparse
import os
from mtcnn.mtcnn import MTCNN
import matplotlib.pyplot as plt
from PIL import Image
import math
from functions import *
from argparse import ArgumentParser

parser = ArgumentParser()
parser.add_argument("--input_image", type=str)
args = parser.parse_args()

path = "/content/drive/MyDrive/ImageProcessing/Assignment-27"

#---------------salt_and_pepper_noise

# img = cv2.imread(args.input_image)
img = cv2.imread(args.input_image)
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
img_gray_copy = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
img_gray_copy1 = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

noise_mask =  np.random.randint(0, 21, size = (img_gray.shape[0], img_gray.shape[1]), dtype=int)

zeros_pixel = np.where(noise_mask == 0)
one_pixel = np.where(noise_mask == 20)

img_gray[zeros_pixel] = 0
img_gray[one_pixel] = 255

cv2_imshow(img_gray)
cv2.imwrite(os.path.join(path, "result/salt_and_pepper_mr_bean.jpg"), img_gray)

#---------------remove noise

img_without_noise = cv2.medianBlur(img_gray, 3)
cv2_imshow(img_without_noise)
cv2.imwrite(os.path.join(path, "result/remove_salt_and_pepper_mr_bean.jpg"), img_without_noise)
