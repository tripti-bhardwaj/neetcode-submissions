class Solution:
    def hammingWeight(self, n: int) -> int:
        count = 0
        n = list(f"{n:b}")
        for i in n:
            if i == '1':
                count += 1
        return count