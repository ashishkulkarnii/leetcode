class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = dict()
        for i, n in enumerate(nums):
            try:
                return [i, seen[target - n]]
            except:
                seen[n] = i
