#Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

#An input string is valid if:

#1. Open brackets must be closed by the same type of brackets.
#2. Open brackets must be closed in the correct order.
#3. Every close bracket has a corresponding open bracket of the same type.

class Solution(object):
    def isValid(self, s):
        try:
            stack = []
            for i in range(len(s)):
                
                if s[i] == "(":
                    stack.append("(")

                if s[i] == "[":
                    stack.append("[")

                if s[i] == "{":
                    stack.append("{") 

                if s[i] == ")":
                    if stack[-1] != "(":
                        return False
                    stack = stack[:-1]

                if s[i] == "]":
                    if stack[-1] != "[":
                        return False
                    stack = stack[:-1]

                if s[i] == "}":
                    if stack[-1] != "{":
                        return False
                    stack = stack[:-1]   

            if stack != []:
                return False
            return True   

        except:
            return False 
