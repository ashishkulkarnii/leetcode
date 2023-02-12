class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        replace = dict()
        for i, c in enumerate(t):
            if c in replace.keys():
                if s[i] != replace[c]:
                    return False
            else:
                replace[c] = s[i]
        s, t = t, s
        replace = dict()
        for i, c in enumerate(t):
            if c in replace.keys():
                if s[i] != replace[c]:
                    return False
            else:
                replace[c] = s[i]
        return True