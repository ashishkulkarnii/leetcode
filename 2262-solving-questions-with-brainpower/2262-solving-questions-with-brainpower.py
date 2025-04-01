class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        dp = [points for points, bp in questions]
        for i in range(len(questions) - 1, -1, -1):
            points, bp = questions[i]
            if i + bp + 1 < len(dp):
                dp[i] = dp[i] + dp[i+bp+1]
            if i + 1 < len(dp):
                dp[i] = max(dp[i], dp[i+1])
        return dp[0]
