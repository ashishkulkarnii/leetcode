class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        smallest_till = [nums[0]]
        for n in nums[1:]:
            smallest_till.append(min(smallest_till[-1], n))
        largest_after = [nums[-1]]
        for n in nums[::-1][1:-1]:
            largest_after.insert(0, max(largest_after[0], n))
        res = 0
        for i, l in enumerate(largest_after):
            res = max(res, l - smallest_till[i])
        if res:
            return res
        else:
            return -1