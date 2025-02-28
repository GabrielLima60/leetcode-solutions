'''
  Given an array nums of distinct integers, return all the possible
permutations.
  You can return the answer in any order.
'''

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        self.nums = nums
        self.result = []
        self.path = []
        self.backtrack()
        return self.result

    def backtrack(self):
        for number in self.nums:
            if number not in self.path:
                self.path.append(number)
                if len(self.path) == len(self.nums):
                    self.result.append(self.path[:])
                else:
                    self.backtrack()
                self.path.pop()
