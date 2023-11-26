'''Given an integer x, return true if x is a palindrome, and false otherwise.'''

class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False

        x = str(x)

        for i in range(len(x)//2):
            if x[i] == x[-i - 1]:
                continue
            else:
                return False
        
        return True
