class Solution:
    def checkDistances(self, s: str, distance: List[int]) -> bool:
        d = [-1 for _ in range(26)]
        for i, c in enumerate(list(s)):
            if d[ord(c) - ord('a')] != -1:
                d[ord(c) - ord('a')] = i - d[ord(c) - ord('a')] - 1
            else:
                d[ord(c) - ord('a')] = i
        for i in range(len(d)):
            if distance[i] != d[i]:
                if d[i] != -1:
                    return False
        return True