'''
Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), return the number of islands.

An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.
'''

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        self.number_of_ones = 0
        self.grid = grid

        for m in range(len(self.grid)):
            for n in range(len(self.grid[0])):
                if self.grid[m][n] == "1":
                    self.number_of_ones +=1
                    self.destroy_ones(m, n)
        return self.number_of_ones
        
    
    def destroy_ones(self, m, n):
        if m < 0 or m >= len(self.grid) or n < 0 or n >= len(self.grid[0]):
            return

        if self.grid[m][n] == "1":
            self.grid[m][n] = "#"

            self.destroy_ones(m - 1, n)    
            self.destroy_ones(m, n - 1)
            self.destroy_ones(m + 1, n)
            self.destroy_ones(m, n + 1)

        else:
            return
