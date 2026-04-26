class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        f = [0 for _ in range(26)]
        for c in s:
            f[ord(c) - ord('a')] += 1
        for c in t:
            f[ord(c) - ord('a')] -= 1
        return all(freq == 0 for freq in f)