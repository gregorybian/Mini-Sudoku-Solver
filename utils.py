import cv2 as cv
import pytesseract as pt

def preprocessing(img):
    image = cv.imread(img)
    image = cv.resize(image, (2000, 2000))
    image = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
    return image

# Uses a threshold value to determine all the contours and finds the contours with the greatest area then assigns the index positions to c
def getBW(img):
    _, thresh = cv.threshold(img, 100, 255, cv.THRESH_BINARY)
    return thresh
    

# This function combines the points gathered from the contour edges into the main 4 corners of the sudoku grid
# IMPORTANT: Adjust threshold to a reasonable value given fluctuation in pixel position.
def findCorners(thresh):
    contours, _ = cv.findContours(thresh, cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE)
    c = max(contours, key = cv.contourArea)

    i = 0
    threshold = 15
    corners = {
        "x_min": 0,
        "x_max": 0,
        "y_min": 0,
        "y_max": 0
    }

    # This while loop goes through the corners array that is generated and elimates duplicate corners that are caused by rounded edges
    while i < len(c)-1:
        if c[i][0][0] - c[i+1][0][0] < -threshold:
            corners["x_max"] = c[i+1][0][0]
            corners["x_min"] = c[i][0][0]

        if c[i][0][1] - c[i+1][0][1] < -threshold:
            corners["y_max"] = c[i+1][0][1]
            corners["y_min"] = c[i][0][1]
        i+=1
    
    return corners


# Use array slicing to get each image isolated to be processed by the Optical Character Recognition library
# 30 was used to shrink each box so that the image was clear for the OCR to detect
# Returns a 2d array corresponding to the sudoku board that was inputted
def getBoard(corners, img):
    height = (corners["y_max"] - corners["y_min"])/6
    width = (corners["x_max"] - corners["x_min"])/6

    sudoku_board = [[0]*6 for _ in range(6)]

    for i in range(6):
        for j in range(6):
            x1 = int(corners["x_min"] + (i * width)+30)
            x2 = int(corners["x_min"] + ((i+1)* width)-30)
            y1 = int(corners["y_min"] + (j * height)+30)
            y2 = int(corners["y_min"] + ((j+1)*height)-30)

            temp_img = img[y1:y2, x1:x2]
            temp_img = cv.resize(temp_img,(300,300))

            cv.imshow("img", temp_img)

            text = pt.image_to_string(temp_img, config="--psm 8 digits")
            sudoku_board[j][i] = text.strip()

    # Make all the values into integers
    sudoku_board = [
        [int(float(x)) if x else 0 for x in row]
        for row in sudoku_board
    ]
    return sudoku_board