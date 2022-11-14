class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        res = set()
        for n in nums:
            if n in res:
                res.remove(n)
            else:
                res.add(n)
        return list(res)