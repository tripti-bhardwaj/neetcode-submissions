class Solution:
    def calPoints(self, operations: List[str]) -> int:
        record = []
        push = record.append
        pop = record.pop
        for op in operations:
            if op == "+":
                push(record[-1] + record[-2])
            elif op == "D":
                push(2 * record[-1])
            elif op == "C":
                pop()
            else:
                push(int(op))
        return sum(record)
