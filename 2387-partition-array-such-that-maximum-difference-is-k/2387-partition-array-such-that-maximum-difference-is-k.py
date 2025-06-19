class Solution:
    def partitionArray(self, nums: List[int], k: int) -> int:
        nums.sort()
        lmin, lmax = nums[0], nums[0]
        res = 0
        for n in nums:
            lmin, lmax = min(lmin, n), max(lmax, n)
            if lmax - lmin > k:
                res += 1
                lmin, lmax = n, n
        return res + 1