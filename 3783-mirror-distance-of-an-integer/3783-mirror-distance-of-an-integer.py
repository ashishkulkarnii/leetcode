class Solution:
    def mirrorDistance(self, n: int) -> int:
        def reverse(n):
            res = 0
            while n > 0:
                res = res * 10 + n % 10
                n //= 10
            return res
        return abs(n - reverse(n))