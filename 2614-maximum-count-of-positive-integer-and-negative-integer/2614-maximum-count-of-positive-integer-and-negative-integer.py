class Solution:
    def maximumCount(self, nums: List[int]) -> int:
        p, n = 0, 0
        for num in nums:
            p += num > 0
            n += num < 0
        return max(p, n)