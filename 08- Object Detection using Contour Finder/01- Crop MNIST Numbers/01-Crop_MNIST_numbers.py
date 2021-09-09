
import numpy as np
import cv2
from google.colab.patches import cv2_imshow
import argparse
from argparse import ArgumentParser
import os
from argparse import ArgumentParser

path = "/content/drive/MyDrive/ImageProcessing/Assignment-26"

parser = ArgumentParser()
parser.add_argument("--MNIST_numbers", type=str)
args = parser.parse_args()

img = cv2.imread(args.MNIST_numbers)
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

#---------remove_noise

thresh = cv2.adaptiveThreshold(img_gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV, 57, 5)
thresh = 255 - thresh

contours = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
contours = contours[0] if len(contours) == 2 else contours[1]

for cnt in contours:
    area = cv2.contourArea(cnt)

    if area < 3:
        cv2.drawContours(thresh, [cnt], -1, (0,0,0), -1)


#---------number of rows and columns

thresh = 255 - thresh
contours = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
contours = contours[0] if len(contours) == 2 else contours[1]


num_columns = 0
num_rows = 0
n_r = 0
n_c = 0
flag = 0

numbers = []

for cnt in contours:

    area = cv2.contourArea(cnt)
    x, y, w, h = cv2.boundingRect(cnt)

    if area > 70:

        if flag == 0:
            n_r = x
            n_c = y
            
        if x >  n_r - 10 and x <  n_r + 10:
            num_rows = num_rows + 1            
              
        if area > 110:          

            if y >  n_c - 10 and y <  n_c + 10:
                num_columns = num_columns + 1               
    flag = 1

stride_in_rows = img_gray.shape[0] // num_rows
stride_in_columns = img_gray.shape[1] // num_columns

#--------------crop and save images

images = []
number = 0
rows = 1

for i in range(0, img_gray.shape[0], stride_in_rows):
    for j in range(0, img_gray.shape[1], stride_in_columns):

        img = img_gray[i: i + stride_in_rows, j: j + stride_in_columns]
        images.append(img)

        if rows %5 == 0 and j == img_gray.shape[1]-stride_in_columns:

            directory = os.path.join(path, "Result/MNIST/", f"numbers_{number}")

            if not os.path.exists(directory):
                os.makedirs(directory)

            for k in range(len(images)):
                cv2.imwrite(os.path.join(directory, f"{k+1}_" + f"{number}.jpg"), images[k])

            images = []
            number = number+1

    rows = rows+1