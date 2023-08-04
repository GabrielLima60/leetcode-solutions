#A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.
#Given a string s, return true if it is a palindrome, or false otherwise.

import math

class Solution:
    def isPalindrome(self, s: str) -> bool:
        alphanum = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

        s = s.lower()
        string = [letter for letter in s if letter in alphanum]
        
        for i in range(math.floor(len(string)/2)):
            if string[i] != string[-i - 1]:
                return False
        
        return True
