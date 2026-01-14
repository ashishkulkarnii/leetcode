class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        n = len(nums)
        disp = set(range(1, n + 1))
        for x in nums:
            if x in disp:
                disp.remove(x)
        return list(disp)