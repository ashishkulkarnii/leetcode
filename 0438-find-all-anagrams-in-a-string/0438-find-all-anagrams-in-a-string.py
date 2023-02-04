class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        p = sorted(p)
        res = []
        for i in range(0, len(s) - len(p) + 1):
            if sorted(s[i:i+len(p)]) == p:
                res.append(i)
        return res