class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort(reverse = True)
        a, b, c = inf, inf, inf
        for x in nums:
            a, b, c = x, a, b
            if a + b > c:
                return a + b + c
        return 0