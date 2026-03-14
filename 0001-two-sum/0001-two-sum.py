class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_pos = {}
        for i, n in enumerate(nums):
            if target - n in num_pos.keys():
                return [i, num_pos[target-n]]
            else:
                num_pos[n] = i
        