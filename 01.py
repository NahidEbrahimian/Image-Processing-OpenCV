import numpy as np
import matplotlib.pyplot as plt

chess_board = np.zeros((10, 10))

for i in range(chess_board.shape[0]):
  for j in range(chess_board.shape[1]):
    
    if i%2 == 0:

      if j%2 == 0:
        chess_board[i, j] = 1
      elif j%2 == 1:
        chess_board[i, j] = 0


    if i%2 == 1:

      if j%2 == 0:
        chess_board[i, j] = 0
      elif j%2 == 1:
        chess_board[i, j] = 1

plt.imshow(chess_board)