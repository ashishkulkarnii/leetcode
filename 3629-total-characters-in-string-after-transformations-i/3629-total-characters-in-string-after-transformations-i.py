class Solution:
    def lengthAfterTransformations(self, s: str, t: int) -> int:
        def inx(c):
            return ord(c) - ord('a')
        
        res = len(s)
        mod = 10 ** 9 + 7
        count = [0] * 26

        for c in list(s):
            count[inx(c)] += 1
        
        for _ in range(t):
            tmp = [0] * 26
            for i, cnt in enumerate(count):
                if i < 25:
                    tmp[i+1] += count[i]
                else:
                    tmp[0] += count[i]
                    tmp[1] += count[i]
            count = tmp
        
        return sum(count) % mod
