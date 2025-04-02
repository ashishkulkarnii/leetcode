class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = [0 for _ in nums]
        dp[-1] = 1
        for i in range(len(nums) - 2, -1, -1):
            sqs = [dp[j] for j, n in list(enumerate(nums))[i+1:] if n > nums[i]]
            if sqs:
                dp[i] = max(sqs)
            dp[i] += 1
        return max(dp)
