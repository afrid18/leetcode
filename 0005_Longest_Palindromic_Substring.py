# Brute force solution:
class Solution:
    def longestPalindrome(self, s: str) -> str:
        lp = s[0]
        for i in range(len(s)):
            for j in range(i + 1, len(s) + 1):
                temp = s[i:j]
                if s[i:j] == temp[::-1] and len(s[i:j]) > len(lp):
                    lp = s[i:j]
        return lp
