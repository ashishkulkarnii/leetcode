class Solution:
    def by2(self, arr):
        for i in range(len(arr)):
            arr[i] = int(arr[i] / 2)
        return arr
    def minOperations(self, nums: List[int]) -> int:
        op = 0
        while nums.count(0) != len(nums):
            for i in range(len(nums)):
                if nums[i] % 2 == 1:
                    nums[i] -= 1
                    op += 1
            if nums.count(0) != len(nums):
                nums = self.by2(nums)
                op += 1
        return op