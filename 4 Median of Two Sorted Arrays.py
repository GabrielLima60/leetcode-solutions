#Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.
#The overall run time complexity should be O(log (m+n)).

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums3 = nums1 + nums2
        nums3 = sorted(nums3)

        middle = len(nums3) // 2

        if len(nums3) % 2 == 1:
            return nums3[middle]

        else:
            return (nums3[middle] + nums3[middle-1]) / 2
