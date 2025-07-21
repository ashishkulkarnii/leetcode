class Solution:
    def makeFancyString(self, s: str) -> str:
        c, f = s[0], 0
        i = 0
        while i < len(s):
            if s[i] == c:
                f += 1
            else:
                c = s[i]
                f = 1
            if f >= 3:
                s = s[:i] + s[i+1:]
                f -= 1
            else:
                i += 1
        return s