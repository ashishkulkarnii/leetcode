class Solution:
    def maxAdjacentDistance(self, nums: List[int]) -> int:
        ans = abs(nums[0] - nums[-1])
        for i in range(len(nums) - 1):
            ans = max(ans, abs(nums[i] - nums[i+1]))
        return ans