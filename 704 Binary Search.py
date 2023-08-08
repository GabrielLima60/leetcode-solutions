#Given an array of integers nums which is sorted in ascending order, and an integer target, write a function to search target in nums. If target exists, then return its index. Otherwise, return -1.
#You must write an algorithm with O(log n) runtime complexity.

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        idx = 0

        while True:
            middle = len(nums) // 2
            if target not in nums:
                return -1

            elif nums[middle] == target:
                return middle + idx 
            
            elif nums[middle] > target:
                nums = nums[:middle]
            
            else:
                nums = nums[middle:]
                idx += middle
