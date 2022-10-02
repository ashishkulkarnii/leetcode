class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        return len(set(nums)) - 1 if nums.count(0) else len(set(nums))