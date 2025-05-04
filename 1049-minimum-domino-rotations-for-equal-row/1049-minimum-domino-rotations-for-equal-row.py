class Solution:
    def minDominoRotations(self, tops: List[int], bottoms: List[int]) -> int:
        potent = set([tops[0], bottoms[0]])
        n = len(tops)
        for i in range(1, n):
            potent = potent & set([tops[i], bottoms[i]])
            if not potent:
                return -1
        res = n
        while potent:
            a = potent.pop()
            tmp = 0
            for x in tops:
                tmp += x == a
            tmp = min(tmp, n - tmp)
            res = min(res, tmp)
            tmp = 0
            for x in bottoms:
                tmp += x == a
            tmp = min(tmp, n - tmp)
            res = min(res, tmp)
        return res