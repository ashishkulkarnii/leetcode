class Solution:
    def bestTeamScore(self, scores: List[int], ages: List[int]) -> int:
        x = sorted(zip(ages, scores))
        n = len(x)
        dp = [0] * n
        for i in range(n):
            dp[i] = x[i][1]
            for j in range(i):
                if x[i][1] >= x[j][1]:
                    dp[i] = max(dp[i], dp[j] + x[i][1])
        return max(dp)