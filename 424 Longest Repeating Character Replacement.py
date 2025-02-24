'''
You are given a string s and an integer k. You can choose any character of the string and change it to any other uppercase English character. You can perform this operation at most k times.

Return the length of the longest substring containing the same letter you can get after performing the above operations.
'''

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        if len(s) <= k:
            return len(s)
        elif len(s) == 1:
            return 1

        longest_repeating = 0
        left_border = 0
        count = [0] * 26

        for right_border in range(len(s)):

            count[ord(s[right_border]) - ord('A')] += 1
            amount = max(count)

            if right_border - left_border + 1 - amount > k:
                count[ord(s[left_border]) - ord('A')] -= 1
                left_border += 1
            
            longest_repeating = max(longest_repeating,amount + k)           

        return min(longest_repeating, len(s))
