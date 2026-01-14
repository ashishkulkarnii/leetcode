class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        # could be O(nlogn) using sorting and binary search
        res = []
        for i in nums:
            x = 0
            for j in nums:
                if j < i:
                    x += 1
            res.append(x)
        return res