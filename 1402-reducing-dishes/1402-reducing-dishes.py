class Solution:
    def maxSatisfaction(self, satisfaction: List[int]) -> int:
        satisfaction.sort()
        max = 0
        temp = 0
        for i in range(0, len(satisfaction)-1):
            for j in range(i, len(satisfaction)):
                temp += (j+1-i) * satisfaction[j]
            if temp > max:
                max = temp
            temp = 0
        return max