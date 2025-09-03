import cv2 as cv
import numpy as np
#from utils.py import *
import pytesseract as pt


# Creating the Image

img = cv.imread("images/1.png")
img = cv.resize(img, (2000, 2000))
img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

blank = np.zeros(img.shape, dtype="uint8")


# Uses a threshold value to determine all the contours and finds the contours with the greatest area then assigns the index positions to c
ret, thresh = cv.threshold(img, 100, 255, cv.THRESH_BINARY)

contours, hierarchies = cv.findContours(thresh, cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE)
c = max(contours, key = cv.contourArea)


# This function combines the points gathered from the contour edges into the main 4 corners of the sudoku grid
# IMPORTANT: Adjust threshold to a reasonable value given fluctuation in pixel position.

i = 0
prev_i = -1
threshold = 15
x_total = 0
y_total = 0
corners = {
    "x_min": 0,
    "x_max": 0,
    "y_min": 0,
    "y_max": 0
}



while i < len(c)-1:
    if c[i][0][0] - c[i+1][0][0] < -threshold:
        corners["x_max"] = c[i+1][0][0]
        corners["x_min"] = c[i][0][0]

    if c[i][0][1] - c[i+1][0][1] < -threshold:
        corners["y_max"] = c[i+1][0][1]
        corners["y_min"] = c[i][0][1]
    i+=1



height = (corners["y_max"] - corners["y_min"])/6
width = (corners["x_max"] - corners["x_min"])/6

print(height, width)


sudoku_board = [[0]*6 for _ in range(6)]
# [columns][rows]

for i in range(6):
    for j in range(6):
        x1 = int(corners["x_min"] + (i * width)+30)
        x2 = int(corners["x_min"] + ((i+1)* width)-30)
        y1 = int(corners["y_min"] + (j * height)+30)
        y2 = int(corners["y_min"] + ((j+1)*height)-30)

        temp_img = thresh[y1:y2, x1:x2]
        temp_img = cv.resize(temp_img,(300,300))

        text = pt.image_to_string(temp_img, config="--psm 8 digits")
        sudoku_board[j][i] = text.strip()


print(sudoku_board)



cv.waitKey(0)