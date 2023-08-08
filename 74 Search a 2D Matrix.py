#You are given an m x n integer matrix matrix with the following two properties:
#Each row is sorted in non-decreasing order.
#The first integer of each row is greater than the last integer of the previous row.
#Given an integer target, return true if target is in matrix or false otherwise.
#You must write a solution in O(log(m * n)) time complexity.



class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        while True:
            middle = len(matrix) // 2
            if target in matrix[middle]:
                return True
            
            elif len(matrix) <= 1:
                return False
            
            elif target < matrix[middle][0]:
                matrix = matrix[:middle]

            else:
                matrix = matrix[middle:]
