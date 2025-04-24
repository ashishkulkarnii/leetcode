class Solution:
    def countCompleteSubarrays(self, nums: List[int]) -> int:
        n = len(nums)
        n_unique = len(set(nums))
        res = 0
        for i in range(n):
            c = set()
            for j in range(i, n):
                c.add(nums[j])
                if len(c) == n_unique:
                    res += n - j
                    break
        return res
