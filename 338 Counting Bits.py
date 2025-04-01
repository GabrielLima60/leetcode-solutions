'''
Given an integer n, return an array ans of length n + 1 such that for each i (0 <= i <= n), ans[i] is the number of 1's in the binary representation of i.
'''

class Solution:
    def countBits(self, n: int) -> List[int]:
        result = [0] * (n+1)

        for i in range(n+1):
            result[i] = result[i >> 1] + (i & 1)

        return result
