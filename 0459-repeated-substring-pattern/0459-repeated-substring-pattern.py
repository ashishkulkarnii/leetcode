class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        for i in range(len(s) // 2, 0, -1):
            if len(s) % i != 0:
                continue
            if s[:i:] * (len(s) // i) == s:
                return True
        return False