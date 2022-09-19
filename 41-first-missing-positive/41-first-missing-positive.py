class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        nums.sort()
        x = 1
        for i in nums:
            if x == i:
                x += 1
        return x