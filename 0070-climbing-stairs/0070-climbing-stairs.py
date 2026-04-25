class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        if n == 2:
            return 2
        x, y, z = 1, 2, 3
        for i in range(2, n):
            z = x + y
            x = y
            y = z
        return z