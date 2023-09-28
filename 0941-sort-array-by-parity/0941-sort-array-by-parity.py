class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        res = []
        for n in nums:
            if n % 2:
                res.append(n)
            else:
                res.insert(0, n)
        return res