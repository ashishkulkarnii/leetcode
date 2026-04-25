class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        i, j = 0, 0
        text1 = s
        text2 = s[::-1]
        m, n = len(text1), len(text2)
        dp = [[0 for _ in range(n)] for _ in range(m)]
        dp[i][j] == max(dp[i-1][j], dp[i][j-1]) + (text1[i] == text2[j])
        for i in range(m):
            for j in range(n):
                if text1[i] == text2[j]:
                    dp[i][j] = (dp[i-1][j-1] if i > 0 and j > 0 else 0) + 1
                else:
                    dp[i][j] = max((dp[i-1][j] if i > 0 else 0), (dp[i][j-1] if j > 0 else 0))
        return dp[-1][-1]