class Solution:
    def rob(self, nums: List[int]) -> int:
        def rob1(nums):
            x, y = nums[0], max(nums[0], nums[1])
            for i in range(2, len(nums)):
                z = max(x + nums[i], y)
                x = y
                y = z
            return y
        match len(nums):
            case 1:
                return nums[0]
            case 2:
                return max(nums)
            case _:
                return max(rob1(nums[1:]), rob1(nums[:-1]))