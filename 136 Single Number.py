'''
Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.

You must implement a solution with a linear runtime complexity and use only constant extra space.
'''

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        found = 0

        # XOR is absolute witchcraft
        for number in nums:
            found ^= number
        return found
