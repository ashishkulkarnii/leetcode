class Solution:
    def largestGoodInteger(self, num: str) -> str:
        res = "/"
        i = 0
        while i < len(num) - 3:
            if num[i] > res[0] and  num[i] == num[i+1] == num[i+2]:
                res = num[i] * 3
            i += 1
        return "" if res == "/" else res