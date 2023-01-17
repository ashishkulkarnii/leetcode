class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        i = 0
        z = 0
        while i < len(nums):
            if nums[i] == 0:
                nums.pop(i)
                z += 1
            else:
                i += 1
        for i in range(z):
            nums.append(0)
        