'''
You are climbing a staircase. It takes n steps to reach the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?
'''
class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 3:
            return n
        number_steps = [1, 2, 3]

        for i in range(3, n):
            number_steps.append(number_steps[1] + number_steps[2])
            number_steps.remove(number_steps[0])

        
        return number_steps[-1]
