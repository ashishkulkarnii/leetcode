class Solution:
    def minOperations(self, grid: List[List[int]], x: int) -> int:
        nums = [n for row in grid for n in row]
        n = len(nums)
        mean = statistics.median(nums)
        closest = nums[0]
        for i in range(n):
            if abs(nums[i] - mean) < abs(mean - closest):
                closest = nums[i]
        res = 0
        for num in nums:
            dist = abs(num - closest)
            if dist % x:
                return -1
            res += dist // x                
        return res