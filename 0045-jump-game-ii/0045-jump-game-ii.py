class Solution:
    def jump(self, nums: List[int]) -> int:
        dp = [0 for n in nums]
        for i in range(len(nums) - 2, -1, -1):
            reachable = dp[i+1:i+1+nums[i]]
            if reachable:
                dp[i] = min(reachable) + 1
            else:
                dp[i] = math.inf
        return dp[0]