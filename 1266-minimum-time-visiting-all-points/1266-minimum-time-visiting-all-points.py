class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        xi, yi = points[0]
        res = 0
        for x, y in points[1::]:
            dx = abs(x - xi)
            dy = abs(y - yi)
            while dx > 0 and dy > 0:
                res += 1
                dx -= 1
                dy -= 1
            if dx > 0:
                res += dx
            elif dy > 0:
                res += dy
            xi = x
            yi = y
        return res