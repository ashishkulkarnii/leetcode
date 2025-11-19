class Solution:
    def findFinalValue(self, nums: List[int], original: int) -> int:
        n = [0] * max(nums)
        for x in nums:
            n[x-1] = 1
        while original - 1 < len(n) and n[original-1]:
            original *= 2
        return original