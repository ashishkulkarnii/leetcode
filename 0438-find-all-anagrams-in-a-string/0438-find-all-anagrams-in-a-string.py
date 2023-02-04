class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if len(s) < len(p):
            return []
        
        res = []
        
        freq = [0] * 26
        for c in p:
            freq[ord(c) - ord('a')] += 1
        
        
        slide = [0] * 26
        for i in range(0, len(p)):
            slide[ord(s[i]) - ord('a')] += 1
        if slide == freq:
            res.append(0)
        
        for i in range(1, len(s) - len(p) + 1):
            slide[ord(s[i-1]) - ord('a')] -= 1
            slide[ord(s[i+len(p)-1]) - ord('a')] += 1
            if slide == freq:
                res.append(i)
        
        return res