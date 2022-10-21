class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        r = 0
        max_length = 0
        while r < len(s):
            c = s[r]
            while c in s[l:r]:
                l += 1
            max_length = max(max_length, r - l + 1)
            r += 1
        return max_length
