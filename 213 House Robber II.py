'''
You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed. All houses at this place are arranged in a circle. That means the first house is the neighbor of the last one. Meanwhile, adjacent houses have a security system connected, and it will automatically contact the police if two adjacent houses were broken into on the same night.

Given an integer array nums representing the amount of money of each house, return the maximum amount of money you can rob tonight without alerting the police.
'''

class Solution:
    def rob(self, nums: List[int]) -> int:
        nums_no_first = nums[:3]

        if len(nums) <= 3:
            return max(nums)

        nums_no_first.append(nums[3] + nums[1])
        nums[3] += max(nums[0], nums[1])

        if len(nums) > 3:
            nums[2] += nums[0]
            for i in range(4, len(nums)):
                nums_no_first.append(nums[i] + max(nums_no_first[i-2], nums_no_first[i-3]))
                nums[i] += max(nums[i-2], nums[i-3]) 
            
        return max(nums[-2], nums[-3], nums_no_first[-1],  nums_no_first[-2])
