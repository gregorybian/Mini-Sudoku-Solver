import cv2 as cv
import numpy as np
import utils
import solver


# Process the Image to be the right size and color (Black and White)
img = utils.preprocessing("images/2.png")
img = utils.getBW(img)

# Get the corners in the corner dictionary
corners = utils.findCorners(img)


# Get the 2d array of the sudoku puzzle
sudoku_board = utils.getBoard(corners, img)
solver.printBoard(sudoku_board)

# Solve the board
solver.solve(sudoku_board)
solver.printBoard(sudoku_board)


cv.waitKey(0)