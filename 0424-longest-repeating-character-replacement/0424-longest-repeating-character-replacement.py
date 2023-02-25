class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        chars = [0] * 26
        lo = 0
        res = 0
        for hi in range(0, len(s)):
            chars[ord(s[hi]) - ord('A')] += 1
            if max(chars) <= hi - lo + 1 <= k + max(chars):
                res = max(res, hi - lo + 1)
            elif hi - lo + 1 > k + max(chars):
                chars[ord(s[lo]) - ord('A')] -= 1
                lo += 1
        return res