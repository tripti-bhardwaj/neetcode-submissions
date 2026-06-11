class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 == 1:
            return False
        else: 
            stack = []
            mapping = {')' : '(', ']' : '[', '}' : '{'}

            for bracket in s:
                if bracket in mapping:
                    if stack and stack[-1] == mapping[bracket]:
                        stack.pop()
                    else: 
                        return False
                else:
                    stack.append(bracket)
        return True if not stack else False
            