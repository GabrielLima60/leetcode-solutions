'''
Given an array of integers temperatures represents the daily temperatures, return an array answer such that answer[i] is the number of days you have to wait after the ith day to get a warmer temperature. If there is no future day for which this is possible, keep answer[i] == 0 instead.
'''

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = []
        stack = [[temperatures[-1], len(temperatures) - 1]]

        for day in range(len(temperatures)-1, -1, -1):
            if temperatures[day] >= stack[0][0]:
                stack = [[temperatures[day], day]]
                result.append(0)

            elif temperatures[day] >= stack[-1][0]:
                while temperatures[day] >= stack[-1][0]:
                    stack.pop()

                result.append(stack[-1][1] - day)
                stack.append([temperatures[day], day])

            else:
                stack.append([temperatures[day], day])
                result.append(1)
    
        result.reverse()
        return result
