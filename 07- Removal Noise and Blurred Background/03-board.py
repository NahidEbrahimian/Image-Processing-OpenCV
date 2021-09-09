
import numpy as np
import cv2
from google.colab.patches import cv2_imshow
import argparse
from argparse import ArgumentParser
import os
from argparse import ArgumentParser

path = "/content/drive/MyDrive/ImageProcessing/Assignment-26"

parser = ArgumentParser()
parser.add_argument("--board_image", type=str)
args = parser.parse_args()

img = cv2.imread(args.board_image)
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# cv2_imshow(img_gray)

board_without_noise = cv2.medianBlur(img_gray, 3)
board_without_noise = cv2.medianBlur(board_without_noise, 3)

# cv2_imshow(img_without_noise)
cv2.imwrite(os.path.join(path + "/Result/board.jpg"), board_without_noise)