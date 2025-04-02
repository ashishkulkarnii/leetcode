class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        res = 0
        for k in range(2, len(nums)):
            for j in range(1, k):
                for i in range(0, j):
                    res = max(res, (nums[i] - nums[j]) * nums[k])
        return res