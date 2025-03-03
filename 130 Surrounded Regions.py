'''
You are given an m x n matrix board containing letters 'X' and 'O', capture regions that are surrounded:

Connect: A cell is connected to adjacent cells horizontally or vertically.
Region: To form a region connect every 'O' cell.
Surround: The region is surrounded with 'X' cells if you can connect the region with 'X' cells and none of the region cells are on the edge of the board.
To capture a surrounded region, replace all 'O's with 'X's in-place within the original board. You do not need to return anything.
'''

class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        self.protected = set()
        self.cols = len(board)
        self.rows = len(board[0])

        for m in range(self.cols):
            if board[m][0] == "O":
                self.protect_zeros(board, m, 0)
            if board[m][self.rows - 1] == "O":
                self.protect_zeros(board, m, self.rows - 1)
        for n in range(self.rows):
            if board[0][n] == "O":
                self.protect_zeros(board, 0, n)
            if board[self.cols - 1][n] == "O":
                self.protect_zeros(board, self.cols - 1, n)
            
        for m in range(self.cols):
            for n in range(self.rows):
                if (m, n) not in self.protected:
                    board[m][n] = "X"



    def protect_zeros(self, board, m, n):
        if (m < 0 or n < 0 or m >= self.cols or n >= self.rows):
            return

        elif board[m][n] == "X":
            return 

        elif (m, n) in self.protected:
            return

        self.protected.add((m, n))

        self.protect_zeros(board, m + 1, n) 
        self.protect_zeros(board, m - 1, n) 
        self.protect_zeros(board, m, n + 1) 
        self.protect_zeros(board, m, n - 1) 
