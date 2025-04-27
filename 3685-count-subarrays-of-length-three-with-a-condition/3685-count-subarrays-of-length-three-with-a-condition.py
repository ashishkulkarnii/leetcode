class Solution:
    def countSubarrays(self, nums: List[int]) -> int:
        res = 0
        n = len(nums)
        for i in range(n - 2):
            a = nums[i]
            b = nums[i + 1]
            c = nums[i + 2]
            if (a + c) * 2 == b:
                res += 1
        return res