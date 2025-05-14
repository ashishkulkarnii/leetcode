class Solution:
    def lengthAfterTransformations(self, s: str, t: int) -> int:        
        mod = 1000000007
        count = [0] * 26
        zero = ord('a')

        for c in list(s):
            count[ord(c) - zero] += 1
        
        for _ in range(t):
            tmp = [0] * 26
            for i, cnt in enumerate(count):
                if i < 25:
                    tmp[i+1] += cnt
                else:
                    tmp[0] += cnt
                    tmp[1] += cnt
            count = tmp
        
        return sum(count) % mod
