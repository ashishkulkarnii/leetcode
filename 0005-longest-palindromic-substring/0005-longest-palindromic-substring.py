class Solution:
    def longestPalindrome(self, s: str) -> str:
        dp = [[0 for _ in s] for _ in s]
        n = len(s)
        res = 1
        for l in range(1, n + 1):
            for i in range(0, n - l + 1):
                if l < 3 and s[i] == s[i+l-1]:
                    dp[i][i+l-1] = l
                    res = max(res, l)
                elif dp[i+1][i+l-2] and s[i] == s[i+l-1]:
                    dp[i][i+l-1] = l
                    res = max(res, l)
        for i in range(n):
            for j in range(i, n):
                if dp[i][j] == res:
                    return s[i:j+1]