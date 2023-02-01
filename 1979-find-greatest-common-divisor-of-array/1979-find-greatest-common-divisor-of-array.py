class Solution:
    def findGCD(self, nums: List[int]) -> int:
        least, greatest = nums[0], nums[0]
        for n in nums:
            least = min(least, n)
            greatest = max(greatest, n)
        return math.gcd(least, greatest)