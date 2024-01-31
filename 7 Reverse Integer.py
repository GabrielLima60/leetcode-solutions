#Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.
#Assume the environment does not allow you to store 64-bit integers (signed or unsigned).

class Solution:
    def reverse(self, x: int) -> int:
        str_x = str(abs(x))
        return_int = 0
        if x > 0:
            return_int = int(self.aux(str_x))
        else:
            return_int = int('-' + self.aux(str_x))

        if return_int >= 2**31 - 1 or return_int <= -2**31:
            return 0
        else:
            return return_int
        
    def aux(self, string):
        return_string = ''
        for i in range(len(string)):
            return_string += string[-i-1]
        return return_string
