class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        p = list(p)
        i = 1
        while i < len(p) - 2:
            if p[i] == "*" == p[i+2] and p[i-1] == p[i+1]:
                p.pop(i)
                p.pop(i)
            else:
                i += 1
        p = "".join(p)
        return self._isMatch(s, p)
    def _isMatch(self, s: str, p: str) -> bool:
        if not (s or p):
                return True
        elif len(p) > 1 and p[1] == "*":
            if s and (s[0] == p[0] or p[0] == "."):
                return self.isMatch(s, p[2:]) or self.isMatch(s[1:], p[2:]) or self.isMatch(s[1:], p)
            else:
                return self.isMatch(s, p[2:])        
        elif s and p and (s[0] == p[0] or p[0] == "."):
            return self.isMatch(s[1:], p[1:])
        else:
            return False