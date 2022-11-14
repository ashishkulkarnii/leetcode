class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        nums.sort()
        perfect = list(range(len(nums)))
        for i in range(len(nums)):
            if nums[i] != perfect[i]:
                return perfect[i]
        return len(nums)