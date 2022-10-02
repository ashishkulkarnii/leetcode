class Solution:
    def isStrictlyPalindromic(self, n: int) -> bool:
        x = n
        for base in range(2, n - 1):
            s = ""
            n = x
            while n > 0:
                s = str(n % base) + s
                n = int(n / base)
            if s != s[::-1]:
                return False
        return True