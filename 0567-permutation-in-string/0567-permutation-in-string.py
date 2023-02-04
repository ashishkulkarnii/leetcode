class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1 = sorted(s1)
        for i in range(0, len(s2) + 1 - len(s1)):
            if s2[i] in s1:
                if sorted(s2[i:i+len(s1):]) == s1:
                    return True
        return False