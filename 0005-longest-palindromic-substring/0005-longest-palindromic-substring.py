class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = s[0]
        for i in range(0, len(s) - 1):
            for j in range(i, len(s)):
                if len(res) < j - i + 1 and s[i:j+1] == s[i:j+1][::-1]:
                    if len(res) < len(s[i:j+1]):
                        res = s[i:j+1]
        return res