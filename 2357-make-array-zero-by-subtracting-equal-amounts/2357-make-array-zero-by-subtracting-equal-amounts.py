class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        if nums.count(0):
            return len(set(nums)) - 1
        return len(set(nums))
