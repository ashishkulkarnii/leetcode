class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        time = 0
        i = 0
        while i < len(colors):
            j = i + 1
            while j < len(colors):
                if colors[j] == colors[i]:
                    j += 1
                else: break
            time += max(neededTime[i:j:])
            i = j
        return sum(neededTime) - time