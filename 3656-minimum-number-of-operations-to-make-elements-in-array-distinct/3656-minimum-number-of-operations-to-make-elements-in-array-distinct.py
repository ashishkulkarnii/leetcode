class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        nums_counts = [0 for i in range(101)]
        for n in nums:
            nums_counts[n] += 1
        res = 0
        while max(nums_counts) > 1:
            d = nums[:3]
            for n in d:
                nums_counts[n] -= 1
            nums = nums[3:]
            res += 1
        return res