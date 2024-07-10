'''
Roman numerals are formed by appending the conversions of decimal place values from highest to lowest. Converting a decimal place value into a Roman numeral has the following rules:

If the value does not start with 4 or 9, select the symbol of the maximal value that can be subtracted from the input, append that symbol to the result, subtract its value, and convert the remainder to a Roman numeral.
If the value starts with 4 or 9 use the subtractive form representing one symbol subtracted from the following symbol, for example, 4 is 1 (I) less than 5 (V): IV and 9 is 1 (I) less than 10 (X): IX. Only the following subtractive forms are used: 4 (IV), 9 (IX), 40 (XL), 90 (XC), 400 (CD) and 900 (CM).
Only powers of 10 (I, X, C, M) can be appended consecutively at most 3 times to represent multiples of 10. You cannot append 5 (V), 50 (L), or 500 (D) multiple times. If you need to append a symbol 4 times use the subtractive form.
Given an integer, convert it to a Roman numeral.
'''

class Solution:
    def intToRoman(self, num: int) -> str:
        numStr = str(num)

        if num == 0: 
            return ""

        elif len(numStr) == 4:
            return "M" + self.intToRoman(num-1000)
        
        elif len(numStr) == 3:
            if numStr[0] == '9':
                return "CM" + self.intToRoman(num-900)
            elif numStr[0] == '5' or numStr[0] == '6' or numStr[0] == '7' or numStr[0] == '8':
                return "D" + self.intToRoman(num-500)
            elif numStr[0] == '4':
                return "CD" + self.intToRoman(num-400)
            else: 
                return "C" + self.intToRoman(num-100)

        elif len(numStr) == 2:
            if numStr[0] == '9':
                return "XC" + self.intToRoman(num-90)
            elif numStr[0] == '5' or numStr[0] == '6' or numStr[0] == '7' or numStr[0] == '8':
                return "L" + self.intToRoman(num-50)
            elif numStr[0] == '4':
                return "XL" + self.intToRoman(num-40)
            else: 
                return "X" + self.intToRoman(num-10)

        else:
            if numStr[0] == '9':
                return "IX" + self.intToRoman(num-9)
            elif numStr[0] == '5' or numStr[0] == '6' or numStr[0] == '7' or numStr[0] == '8':
                return "V" + self.intToRoman(num-5)
            elif numStr[0] == '4':
                return "IV" + self.intToRoman(num-4)
            else: 
                return "I" + self.intToRoman(num-1)
