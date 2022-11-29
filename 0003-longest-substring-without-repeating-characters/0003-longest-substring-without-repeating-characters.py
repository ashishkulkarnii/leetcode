class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        r = 0
        ml = 0
        while r < len(s):
            c = s[r]
            while c in s[l:r]:
                l += 1
            ml = max(ml, r - l + 1)
            r += 1
        return ml
