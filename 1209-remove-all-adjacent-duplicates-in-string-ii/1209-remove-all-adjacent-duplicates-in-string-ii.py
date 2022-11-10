class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        i = 0
        while i < len(s) - k + 1:
            if s[i:i+k].count(s[i]) == len(s[i:i+k]):
                s = s[:i:] + s[i+k::]
                i = max(i - k - 1, 0)
            else:
                i += 1
        return s