#There is an integer array nums sorted in ascending order (with distinct values).

#Prior to being passed to your function, nums is possibly rotated at an unknown pivot index k (1 <= k < nums.length) such that the resulting array is [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed). For example, [0,1,2,4,5,6,7] might be rotated at pivot index 3 and become [4,5,6,7,0,1,2].

#Given the array nums after the possible rotation and an integer target, return the index of target if it is in nums, or -1 if it is not in nums.

#You must write an algorithm with O(log n) runtime complexity.

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        first = nums[0]
        current_index = int(len(nums)/2)

        if target == first:
            return 0
        else:
            low = 0
            high = len(nums)-1
            while low <= high:
                print(low)
                print(high)
                print('\n')
                middle = low + (high - low)//2

                if nums[middle] == target:
                    return middle if middle >= 0 else len(nums) + middle
                elif nums[low] > nums[high]:
                    low-=1
                    high-=1
                
                elif nums[middle] < target:
                    low = middle + 1
                    

                elif nums[middle] > target:
                    high = middle - 1
                    
            return -1
