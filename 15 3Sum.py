# Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

# Notice that the solution set must not contain duplicate triplets.

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        output = []

        for num_index in range(len(nums)-2):
            if num_index > 0 and nums[num_index] == nums[num_index - 1]:
                continue

            left = num_index + 1
            right = len(nums) - 1

            while left < right:
                number_sum = nums[num_index] + nums[left] + nums[right]

                if number_sum == 0:
                    output.append([nums[num_index], nums[left], nums[right]])

                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1

                    left += 1
                    right -= 1

                elif number_sum > 0:
                    right -= 1
                
                elif number_sum < 0:
                    left += 1

        return output
