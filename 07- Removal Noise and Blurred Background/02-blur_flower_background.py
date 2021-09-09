
import numpy as np
import cv2
from google.colab.patches import cv2_imshow
import argparse
from argparse import ArgumentParser
import os
from argparse import ArgumentParser

path = "/content/drive/MyDrive/ImageProcessing/Assignment-26"

parser = ArgumentParser()
parser.add_argument("--flower_image", type=str)
args = parser.parse_args()

img = cv2.imread(args.flower_image)
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

roi = np.where(img_gray>150)

img_blur = cv2.blur(img_gray, (30,30))
img_blur[roi] = img_gray[roi] 

# cv2_imshow(img_blur)

img_blur = cv2.medianBlur(img_blur, 5)
# cv2_imshow(img_blur)

cv2.imwrite(os.path.join(path + "/Result/flower_output.jpg"), img_blur)