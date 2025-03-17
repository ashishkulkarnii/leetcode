class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        seen = set()
        for n in nums:
            if n in seen:
                seen.remove(n)
            else:
                seen.add(n)
        return seen == set()