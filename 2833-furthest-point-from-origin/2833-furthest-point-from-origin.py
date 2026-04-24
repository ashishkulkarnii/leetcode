class Solution:
    def furthestDistanceFromOrigin(self, moves: str) -> int:
        c = collections.Counter(moves)
        return abs(c['R'] - c['L']) + c['_']