class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) < 2:
            return len(s)
        i, j = 0, 0
        res = 1
        seen = set()
        while j < len(s):
            if s[j] not in seen:
                seen.add(s[j])
            else:
                res = max(res, j - i)
                while s[i] != s[j]:
                    seen.remove(s[i])
                    i += 1
                i += 1
            j += 1
        return max(res, j - i)              
