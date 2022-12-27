class Solution:
    def maximumBags(self, capacity: List[int], rocks: List[int], additionalRocks: int) -> int:
        n = len(capacity)
        unused_space = sorted([capacity[i] - rocks[i] for i in range(n)])
        ans = 0
        for i in range(n):
            if unused_space[i] == 0:
                ans += 1
            elif unused_space[i] <= additionalRocks:
                ans += 1
                additionalRocks -= unused_space[i]
        return ans
            