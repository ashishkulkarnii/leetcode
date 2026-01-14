class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        n = len(nums)
        missing = None
        dupe = None
        found = [0] * (n + 1)
        for i in nums:
            found[i] += 1
        for i, c in enumerate(found):
            if i != 0 and c == 0:
                missing = i
            if c == 2:
                dupe = i
        return [dupe, missing]
                
