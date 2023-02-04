class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        c1 = Counter(s1)
        c2 = Counter(s2[:len(s1):])
        if c1 == c2:
            return True
        for i in range(1, len(s2) + 1 - len(s1)):
            c2[s2[i-1]] -= 1
            if c2[s2[i-1]] <= 0:
                del c2[s2[i-1]]
            if s2[i-1+len(s1)] in c2.keys():
                c2[s2[i-1+len(s1)]] += 1
            else:
                c2[s2[i-1+len(s1)]] = 1
            if c1 == c2:
                return True
        return False