class Solution:
    def binaryGap(self, n: int) -> int:
        temp = -1
        res = 0
        n = bin(n)[2::]
        for c in n:
            if c == '1':
                if temp == -1:
                    temp = 0
                else:
                    temp += 1
                    res = max(res, temp)
                    temp = 0
            if c == '0':
                if temp == -1:
                    pass
                else:
                    temp += 1
        return res