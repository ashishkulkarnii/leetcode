class Solution:
    def maximumBags(self, capacity: List[int], rocks: List[int], additionalRocks: int) -> int:
        unused_space = sorted([c - r for c, r in zip(capacity, rocks)])
        ans = 0
        for u in unused_space:
            if u <= additionalRocks:
                ans += 1
                additionalRocks -= u
        return ans
