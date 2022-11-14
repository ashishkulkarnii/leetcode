class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        hm = {}
        for n in nums:
            if n in hm.keys():
                hm[n] += 1
            else:
                hm[n] = 1
        for n, c in hm.items():
            if c == 1:
                return n