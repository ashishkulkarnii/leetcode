class Solution:
    def convertToBase7(self, n: int) -> str:
        if n == 0:
            return '0'
        res = ''
        if n < 0:
            negative = True
            n = -n
        else:
            negative = False
        while n > 0:
            res = str(n % 7) + res
            n = int(n / 7)
        if negative:
            res = '-' + res
        return res