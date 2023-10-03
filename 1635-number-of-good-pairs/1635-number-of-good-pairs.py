from math import factorial

class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        return sum([factorial(c) // (factorial(c-2) * factorial(2)) for c in Counter(nums).values() if c >= 2])
