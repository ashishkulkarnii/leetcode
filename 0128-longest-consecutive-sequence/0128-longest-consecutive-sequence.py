class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        table = dict()
        nums = set(nums)
        res = 0
        for n in nums:
            x = table.get(n - 1, 0)
            y = table.get(n + 1, 0)
            l = x + y + 1
            table[n-x] = l
            table[n+y] = l
            res = max(res, l)
        return res