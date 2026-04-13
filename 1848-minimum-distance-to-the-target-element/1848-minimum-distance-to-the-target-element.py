class Solution:
    def getMinDistance(self, nums: List[int], target: int, start: int) -> int:
        i = 0
        n = len(nums)
        while i < n:
            if 0 <= start - i and nums[start-i] == target or start + i < n and nums[start+i] == target:
                return i
            i += 1