class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones.sort()
        while len(stones) > 1:
            s1 = stones.pop(-1)
            s2 = stones.pop(-1)
            if s1 != s2:
                bisect.insort(stones, s1 - s2)
        return 0 if not stones else stones[0]