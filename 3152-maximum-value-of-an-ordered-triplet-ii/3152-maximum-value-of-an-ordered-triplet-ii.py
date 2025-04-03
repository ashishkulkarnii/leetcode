class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        diff = nums[0] - nums[1]
        max_dp = [nums[0]]
        res = 0
        for k in range(2, len(nums)):
            max_dp.append(max(max_dp[-1], nums[k-1]))
            diff = max(diff, max_dp[k-2] - nums[k-1])
            res = max(res, diff * nums[k])
        return res
