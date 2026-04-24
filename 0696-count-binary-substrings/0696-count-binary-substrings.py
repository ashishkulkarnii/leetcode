class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        i = 0
        n = len(s)
        res = 0
        while i < n:
            c = s[i]
            j = i
            num_c = 0
            num_nc = 0
            while j < n and s[j] == c:
                num_c += 1
                j += 1
            while j < n and s[j] != c:
                num_nc += 1
                j += 1
            res += min(num_c, num_nc)
            i += num_c
        return res