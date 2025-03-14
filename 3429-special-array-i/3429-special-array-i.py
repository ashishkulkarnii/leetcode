class Solution:
    def isArraySpecial(self, nums: List[int]) -> bool:
        for i in range(1, len(nums)):
            if abs(nums[i] - nums[i-1]) % 2 != 1:
                return False
        return True