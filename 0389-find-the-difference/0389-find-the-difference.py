class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        s = list(s)
        t = list(t)
        while s:
            t.remove(s.pop(0))
        return t[0]