class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        h = dict()
        s = s.split()
        if len(s) != len(pattern):
            return False
        for c, w in zip(pattern, s):
            if c in h.keys():
                if h[c] != w:
                    return False
            elif w in h.values():
                return False
            else:
                h[c] = w
        return True