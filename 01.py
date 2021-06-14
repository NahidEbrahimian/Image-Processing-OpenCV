import cv2
import numpy as np
import matplotlib.pyplot as plt


rows = 320
cols = 320

chess_board = np.zeros((rows, cols), dtype = 'uint8')
block_size = chess_board.shape[0] // 8

flag = 0

for i in range(0, rows, block_size):  
    for j in range(0, cols, block_size):

        if flag == 0:
            chess_board[i : i + block_size, j : j + block_size] = 0
            flag = 1

        else:    
            chess_board[i : i + block_size, j : j + block_size] = 255
            flag = 0 
            
    if flag == 0:
      flag = 1

    else:
      flag = 0

plt.imshow(chess_board, cmap = 'gray')
cv2.imwrite("/content/drive/MyDrive/Assignment-21/Results/chess_board.jpg", chess_board)