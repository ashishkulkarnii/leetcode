class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        streak = 0
        mnoco = 0
        for n in nums:
            if n:
                streak += 1
            else:
                mnoco = max(mnoco, streak)
                streak = 0
        return max(mnoco, streak)