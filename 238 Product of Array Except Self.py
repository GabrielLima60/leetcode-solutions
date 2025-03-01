'''
Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

You must write an algorithm that runs in O(n) time and without using the division operation.
'''

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = [1] * len(nums)
        before = 1

        for i in range(len(nums)):
            result[i] *= before
            before *= nums[i]

        after = 1
        for i in range(len(nums)-1, -1, -1):
            result[i] *= after
            after *= nums[i]

        return result
