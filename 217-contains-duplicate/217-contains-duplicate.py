class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        nums.sort()
        while(len(nums) > 1):
            n = nums.pop(0)
            if n == nums[0]:
                return True
        return False