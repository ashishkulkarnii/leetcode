class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        while n > 2:
            if not n % 2:
                n = n / 2
            else: return False
        return n > 0