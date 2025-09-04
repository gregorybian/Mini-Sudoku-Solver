
# Prints the board in the console
def printBoard(board):
    print("Heres your solution!")
    for i in range(len(board)):
        if i % 2 == 0 and i != 0:
            print("-------------")
        
        for j in range(len(board[0])):
            if j % 3 == 0 and j != 0:
                print("| ", end = "")
            if j == 5:
                print(board[i][j])
            else:
                print(str(board[i][j]) + " ", end = "")

# Function that returns the first index position of a number that is 0/unassigned
def findEmpty(board):
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == 0:
                return (i,j) # i is the column, j is the row
    return None

# Function that determines if a number can be in a certain position based on columns, rows, box
# Returns a boolean if number is valid in that position
def checkValid(board, num, pos):
    #Check row
    for i in range(len(board[0])):
        if board[pos[0]][i] == num and pos[1] != i:
            return False

    #Check Column
    for i in range(len(board)):
        if board[i][pos[1]] == num and pos[0] != i:
            return False
        
    #Check Box

    # get which box
    box_y = pos[0] // 2
    box_x = pos[1] // 3
    
    # loop through box and try to find the number
    for i in range(box_y * 2, box_y *2 + 2):
        for j in range(box_x * 3, box_x * 3 + 3):
            if board[i][j] == num and (i,j) != pos:
                return False
 
    return True


# Function that solves the board using previous functions
# Uses backtracking algorithm to try every solution to a square and continue through the grid. If solution doesn't work, algorithm goes to previous number and tries the next number until grid is filled
# Returns a 2d array that is the solution to the problem
def solve(board):
    empty  = findEmpty(board)
    
    #Check if there are empty squares
    if not empty: 
        return True
    else:
        row, col = empty
    
    for i in range(1,7):
        if checkValid(board, i, (row, col)):
            board[row][col] = i

            if solve(board):
                return True
            
            board[row][col] = 0
    return False