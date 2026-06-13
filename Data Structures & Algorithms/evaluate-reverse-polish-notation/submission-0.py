class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        pop = stack.pop
        push = stack.append
        for i in range(len(tokens)):
            if tokens[i] in ('+', '-', '*', '/'):
                operand2 = pop()
                operand1 = pop()
                if tokens[i] == '/':
                    push(int(operand1 / operand2))
                elif tokens[i] == '+':
                    push(operand1 + operand2)
                elif tokens[i] == '-':
                    push(operand1 - operand2)
                else:
                    push(operand1 * operand2)
            else:
                push(int(tokens[i]))
        return stack[0]