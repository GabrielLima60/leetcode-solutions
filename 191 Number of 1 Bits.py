'''
Given a positive integer n, write a function that returns the number of set bits in its binary representation (also known as the Hamming weight).
'''

class Solution:
    def hammingWeight(self, n: int) -> int:
        count = 0
        while n:
            n &= n - 1
            count +=1

        return count
