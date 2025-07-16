class Solution:
    def maximumLength(self, nums: List[int]) -> int:
        nums = [n % 2 for n in nums]
        res = max(nums.count(0), nums.count(1))

        tmp = 0
        start = 0
        for n in nums:
            if n == start:
                tmp += 1
                start = (start + 1) % 2
        res = max(res, tmp)

        tmp = 0
        start = 1
        for n in nums:
            if n == start:
                tmp += 1
                start = (start + 1) % 2
        res = max(res, tmp)

        return res