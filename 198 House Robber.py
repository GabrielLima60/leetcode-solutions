'''
You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed, the only constraint stopping you from robbing each of them is that adjacent houses have security systems connected and it will automatically contact the police if two adjacent houses were broken into on the same night.

Given an integer array nums representing the amount of money of each house, return the maximum amount of money you can rob tonight without alerting the police.
'''

class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) < 3:
            return max(nums)
        elif len(nums) == 3:
            return max(nums[1], nums[0] + nums[2])
        
        else:
            nums[2] += nums[0]
            for i in range(3, len(nums)):
                nums[i] += max(nums[i-2], nums[i-3])
        
            return max(nums[-1], nums[-2])
