# Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.

class Solution(object):
    def topKFrequent(self, nums, k):
        num_freq = {}
        sol = []

        for number in nums:
            num_freq[number] = num_freq.get(number, 0) + 1
        
        for iteration in range(k):
            largest_value = max(num_freq, key=num_freq.get)
            sol.append(largest_value)
            del num_freq[largest_value]
        
        return sol
