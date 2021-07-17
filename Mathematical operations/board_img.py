import numpy as ns
import cv2
import matplotlib.pyplot as plt

board_origin = cv2.imread("board - origin.bmp")
board_test = cv2.imread("board - test.bmp")

board_origin = cv2.cvtColor(board_origin, cv2.COLOR_RGB2GRAY)
board_test = cv2.cvtColor(board_test, cv2.COLOR_RGB2GRAY)

h = board_origin.shape[0]
w = board_origin.shape[1]

board_test_flip = np.zeros_like(board_origin)

for i in range(h):
  for j in range(w):

    board_test_flip[i, j] = board_test[i,  w - j - 1]

board_img = cv2.subtract(board_test_flip, board_origin)

plt.imshow(board_img, cmap = 'gray')

cv2.imwrite(os.path.join(path, "board_img.jpg"), board_img)