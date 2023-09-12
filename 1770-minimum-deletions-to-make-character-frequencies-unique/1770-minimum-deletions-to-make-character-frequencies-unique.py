class Solution:
    def minDeletions(self, s: str) -> int:
        f = sorted(list(Counter(s).values()), reverse=True)
        res = 0
        i = 0
        while i < len(f) - 1:
            if f[i] != 0 and f[i] == f[i+1]:
                f[i+1] -= 1
                res += 1
                f.sort(reverse=True)
            else:
                i += 1
        return res