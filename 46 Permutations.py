'''
  Given an array nums of distinct integers, return all the possible
permutations.
  You can return the answer in any order.
'''

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []
        self.generate_permutations([], nums, result)
        return result

    def generate_permutations(self, basis, nums, result):

        if nums == []:
            result.append(basis)
        else:
            for number in nums:
                self.generate_permutations(basis + [number], [n for n in nums if n != number], result)
