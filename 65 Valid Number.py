'''
Given a string s, return whether s is a valid number.

For example, all the following are valid numbers: "2", "0089", "-0.1", "+3.14", "4.", "-.9", "2e10", "-90E3", "3e+7", "+6e-1", "53.5e93", "-123.456e789", while the following are not valid numbers: "abc", "1a", "1e", "e3", "99e2.5", "--6", "-+3", "95a54e53".

Formally, a valid number is defined using one of the following definitions:

An integer number followed by an optional exponent.
A decimal number followed by an optional exponent.
An integer number is defined with an optional sign '-' or '+' followed by digits.

A decimal number is defined with an optional sign '-' or '+' followed by one of the following definitions:

Digits followed by a dot '.'.
Digits followed by a dot '.' followed by digits.
A dot '.' followed by digits.
An exponent is defined with an exponent notation 'e' or 'E' followed by an integer number.

The digits are defined as one or more digits.
'''

class Solution:

    def __init__(self):
        self.numbers = ["0","1","2","3","4","5","6","7","8","9"]
        self.symbols = ["-","+"]
        self.e = ["e", "E"]
        self.found_dot = False

    def isNumber(self, s: str) -> bool:
        return self.state0(s, 0)

    def state0(self, s, position):
        if s[position] in self.numbers:
            if position == len(s) - 1:
                return True

            return self.state0(s, position + 1)
        
        elif s[position] in self.e:
            if position == 0 or position == len(s) - 1:
                return False
            if s[position - 1] in self.symbols:
                return False
            
            return self.state1(s, position + 1)
        
        elif s[position] in self.symbols:
            if position == 0:
                if position != len(s) - 1:
                    return self.state0(s, position + 1)
            return False
        
        elif s[position] == "." and (position != 0 or position < len(s) - 1):
            if not self.found_dot:
                self.found_dot = True

                if position == len(s) - 1:
                    if s[position - 1] in self.numbers:
                        return True
                    return False
                if s[position + 1] in self.e:
                   if position == 0 or s[position - 1] not in self.numbers:
                        return False 

                return self.state0(s, position + 1)
            return False

        else:
            return False
                
    def state1(self, s, position):
        if s[position] in self.numbers:
            if position == len(s) - 1:
                return True

            return self.state1(s, position + 1)
        
        if s[position] in self.symbols:
            if s[position - 1] in self.e and position < len(s) - 1:
                return self.state1(s, position + 1)
            
        
        return False
        
