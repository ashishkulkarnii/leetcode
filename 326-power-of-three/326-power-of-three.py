class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n == 1:
            return True
        while n > 3:
            if not n % 3:
                n = n / 3
            else: return False
        return n == 3