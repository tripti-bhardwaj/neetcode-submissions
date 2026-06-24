class Solution:
    def scoreOfString(self, s: str) -> int:
        score = 0
        for ch in range(len(s) - 1):
            score += abs(ord(s[ch + 1]) - ord(s[ch]))
        return score

