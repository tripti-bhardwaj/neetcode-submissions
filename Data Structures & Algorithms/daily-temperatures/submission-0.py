class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        stack = []
        push = stack.append
        pop = stack.pop
        for i, t in enumerate(temperatures):
            while stack and t > stack[-1][0]:
                temp, idx = pop()
                res[idx] = (i - idx)
            push([t, i])
        return res
