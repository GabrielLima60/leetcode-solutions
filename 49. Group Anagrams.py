# Given an array of strings strs, group the anagrams together. You can return the answer in any order.
# An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        answer = {}

        for string in strs:
            sorted_string = ''.join(sorted(string))
            if sorted_string not in answer.keys():
                answer[sorted_string] = [string]

            else:
                answer[sorted_string].append(string)


        return answer.values()
