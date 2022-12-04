class Solution:
    def minimumAverageDifference(self, nums: List[int]) -> int:
        prefix = copy.deepcopy(nums)
        suffix = copy.deepcopy(nums)
        n = len(nums)
        for i in range(1, n):
            prefix[i] += prefix[i-1]
            suffix[n-i-1] += suffix[n-i]
        res = sum(nums)
        min_index = -1
        for i in range(n):
            suffix[i] -= nums[i]
            if n - 1 - i > 0:
                if abs(prefix[i]//(i+1) - suffix[i]//(n-1-i)) < res:
                    res = abs(prefix[i]//(i+1) - suffix[i]//(n-1-i))
                    min_index = i
            else:
                if prefix[i]//(i+1) < res:
                    res = prefix[i]//(i+1)
                    min_index = i
        return min_index if min_index >= 0 else 0