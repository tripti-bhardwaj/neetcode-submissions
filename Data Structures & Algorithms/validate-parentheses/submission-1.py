class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 == 1:
            return False
         
        stack = []
        mapping = {')' : '(', ']' : '[', '}' : '{'}

        pop = stack.pop
        push = stack.append
        for bracket in s:
            if bracket in mapping:
                if stack and stack[-1] == mapping[bracket]:
                    pop()
                else: 
                    return False
            else:
                push(bracket)
        return not stack
        