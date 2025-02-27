'''
Given an integer array nums of unique elements, return all possible subsets (the power set).

The solution set must not contain duplicate subsets. Return the solution in any order.
'''

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        self.result = []
        self.nums = nums
        self.aux(0, [])

        return self.result

    def aux(self, start, path):
        self.result.append(path[:])
        for i in range(start, len(self.nums)):
            path.append(self.nums[i])
            self.aux(i+1, path)
            path.pop()
