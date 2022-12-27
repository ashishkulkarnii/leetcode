class Solution:
    def canJump(self, nums: List[int]) -> bool:
        reachable = [False if i > 0 else True for i in range(len(nums))]
        for i, n in enumerate(nums):
            if reachable[i] == True:
                reachable[i+1:i+n+1:] = [True] * n
        return reachable[-1]