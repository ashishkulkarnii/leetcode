class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hm = dict()
        for i, n in enumerate(nums):
            if target - n in hm.keys():
                return [i, hm[target - n]]
            hm[n] = i