class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        dp = [nums[0]]
        for n in nums[1:]:
            dp.append(max(dp[-1] + n, n))
        x = abs(max(dp))
        dp = [nums[0]]
        for n in nums[1:]:
            dp.append(min(dp[-1] + n, n))
        n = abs(min(dp))
        return max(x, n)