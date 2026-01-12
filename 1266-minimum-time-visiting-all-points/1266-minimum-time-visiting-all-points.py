class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        prev = points[0]
        t = 0
        for p in points[1:]:
            x = abs(p[0] - prev[0])
            y = abs(p[1] - prev[1])
            t += max(x, y)
            prev = p
        return t