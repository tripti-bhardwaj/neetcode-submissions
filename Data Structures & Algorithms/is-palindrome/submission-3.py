class Solution:
    def isPalindrome(self, s: str) -> bool:
        nstr = ''
        for ch in s:
            if ch.isalnum():
                nstr += ch.lower()
        return nstr == nstr[::-1]

        