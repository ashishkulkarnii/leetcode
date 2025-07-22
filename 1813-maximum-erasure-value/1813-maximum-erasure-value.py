class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        f = collections.Counter()
        window = []
        wsum = 0
        res = 0
        for i in nums:
            window.append(i)
            wsum += i
            f[i] += 1
            while f[i] > 1:
                f[window[0]] -= 1
                wsum -= window[0]
                window.pop(0)
            res = max(res, wsum)
        return res