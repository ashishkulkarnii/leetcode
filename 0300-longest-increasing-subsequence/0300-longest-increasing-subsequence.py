class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = [0 for _ in nums]
        dp[0] = 1
        n = len(nums)
        res = 0
        for i in range(1, n):
            m = 0
            for j in range(i):
                if nums[i] > nums[j]:
                    m = max(m, dp[j])
            dp[i] = 1 + m
        return max(dp)