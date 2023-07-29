#Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:

#Each row must contain the digits 1-9 without repetition.
#Each column must contain the digits 1-9 without repetition.
#Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.

class Solution(object):
    def isValidSudoku(self, board):

        # Verify lines
        for l in range(9):
            line = board[l]
            line = [x for x in line]
            tester = set()
            for item in line:
                if item != ".":
                    if item in tester:
                        return False
                    tester.add(item)
        
        # Verify columns
        for c in range(9):
            column = [item[c] for item in board]
            tester = set()
            for item in column:
                if item != ".":
                    if item in tester:
                        return False
                    tester.add(item)

        # Verify 3 x 3 sub-boxes
        for column in range(0, 9, 3):
            for line in range(0, 9, 3):
                cube = [board[l][c] for l in range(line, line+3) for c in range(column, column + 3)]
                tester = set()
                for item in cube:
                    if item != ".":
                        if item in tester:
                            return False
                        tester.add(item)

        return True
