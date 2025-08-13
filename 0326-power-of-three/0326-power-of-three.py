class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        while n > 1:
            if not n % 3:
                n = n // 3
            else:
                return False
        return n == 1