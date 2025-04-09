class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        if k > min(nums):
            return -1
        nums = set(nums)
        return len(nums) - int(k in nums)