class Solution:
    def gcdOfStrings(self, a: str, b: str) -> str:
        res = ''
        for i in range(1, len(b) + 1):
            if int(len(a) / i) * b[:i:] == a and int(len(b) / i) * b[:i:] == b:
                res = b[:i:]
        return res