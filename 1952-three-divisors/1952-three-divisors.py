class Solution:
    def isThree(self, n: int) -> bool:
        res = 1
        for i in range(2, n+1):
            if res > 3:
                break
            if n % i == 0:
                res += 1
        return res == 3
                