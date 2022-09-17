class Solution:
    def reverse(self, x: int) -> int:
        n = str(x)
        c = 1
        if n[0] == '-':
            n = n[1::]
            c = -1
        x = int(n[::-1])
        if c*x > 2**31 or c*x < -2**31:
            return 0
        else:
            return c * x