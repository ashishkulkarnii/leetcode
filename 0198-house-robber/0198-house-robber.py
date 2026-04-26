class Solution:
    def rob(self, nums: List[int]) -> int:
        dp = [0 for _ in nums]
        for i in range(len(nums)):
            dp[i] = max(nums[i] + (dp[i-2] if i > 1 else 0), dp[i-1])
        return dp[-1]
