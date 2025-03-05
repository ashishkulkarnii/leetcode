class Solution:
    def findChampion(self, n: int, edges: List[List[int]]) -> int:
        losers = set()
        for w, l in edges:
            losers.add(l)
        winners = [t for t in range(n) if t not in losers]
        return winners[0] if len(winners) == 1 else -1