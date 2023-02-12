class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        left_sum = 0
        right_sum = sum(nums[1::])
        pivot = 0
        while pivot < len(nums):
            if left_sum == right_sum:
                return pivot
            else:
                left_sum += nums[pivot]
                right_sum = 0 if pivot == len(nums) - 1 else right_sum - nums[pivot+1]
                pivot += 1
        return -1