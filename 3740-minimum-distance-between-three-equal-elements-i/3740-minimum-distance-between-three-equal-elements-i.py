class Solution:
    def minimumDistance(self, nums: List[int]) -> int:
        x = collections.defaultdict(list)
        for i, n in enumerate(nums):
            x[n].append(i)
        res = float('inf')
        for l in x.values():
            for i in range(len(l) - 2):
                res = min(res, l[i+2] - l[i])
        return 2 * res if res < float('inf') else -1