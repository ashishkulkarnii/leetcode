class Solution:
    def leftRigthDifference(self, nums: List[int]) -> List[int]:
        sum_arr = sum(nums)
        left_sum = 0
        right_sum = sum_arr - nums[0]
        res = [abs(left_sum - right_sum)]
        for i in range(1, len(nums)):
            left_sum += nums[i-1]
            right_sum -= nums[i]
            res.append(abs(left_sum - right_sum))
        return res