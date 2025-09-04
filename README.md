# Linkedln Mini Sudoku Solver

As a Linkedln warrior, I was captivated by the recently added mini sudoku game. However, contrary to the majority of the mini games where I can score sub 1 minute, the mini sudoku game gave me much more trouble, often taking me over 3 minutes with some times going above 5 minutes. 

Hence I did what any reasonable developer would do, I wrote a script to track each square in the sudoku grid given a screenshot of the game using OpenCV to track the greatest area contour and isolate each square. Then I used the pytesseract library to detect the number in the given square, optimizing for this library (this library was soooo bad at detecting numbers) to return a 2d array containing the value of each square. 

Given that the library was able to detect all the numbers in the grid, the program then uses a backtracking algorithm. This algorithm was designed for efficiency by going through each value choosing a value that works then continuing down the grid. If a value down the grid does not work, the algorithm "backtracks" meaning it goes to the previous number and tries a different value. Hence, I was able to return a completed solution to the minigame!



Feel free to contact me if you have any questions about this script!
