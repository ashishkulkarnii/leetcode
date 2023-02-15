class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        xi, yi = points[0]
        res = 0
        for x, y in points[1::]:
            dx = abs(x - xi)
            dy = abs(y - yi)
            res += (temp := max(dx, dy))
            dx -= temp
            dy -= temp
            if dx > 0:
                res += dx
            elif dy > 0:
                res += dy
            xi = x
            yi = y
        return res