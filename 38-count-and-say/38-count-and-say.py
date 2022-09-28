class Solution:
    def pair(self, n):
        n = str(n)
        prev = n[0]
        count = 1
        res = []
        for i in n[1::]:
            if i == prev:
                count += 1
            else:
                res.append([str(count), prev])
                prev = i
                count = 1
        res.append([str(count), prev])
        return res
    def numFromPairs(self, a):
        res = ""
        for i in a:
            res += i[0] + i[1]
        return res
    def countAndSay(self, n: int) -> str:
        t = 1
        for i in range(n-1):
            t = self.numFromPairs(self.pair(t))
        return str(t)