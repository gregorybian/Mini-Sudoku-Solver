import cv2 as cv
import utils
import solver


# Process the Image to be the right size and color (Black and White)
img = utils.preprocessing("images/1.png")
img = utils.getBW(img)

# Get the corners in the corner dictionary
corners = utils.findCorners(img)

# Get the 2d array of the sudoku puzzle
sudoku_board = utils.getBoard(corners, img)

print(sudoku_board)

# Solve the board



cv.waitKey(0)