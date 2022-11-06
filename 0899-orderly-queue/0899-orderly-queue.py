class Solution:
    def orderlyQueue(self, s: str, k: int) -> str:
        if k > 1:
            return ''.join(sorted(s))
        res = s
        for i, c in enumerate(s):
            if res > s[i::] + s[:i:]:
                res = s[i::] + s[:i:]
        return res