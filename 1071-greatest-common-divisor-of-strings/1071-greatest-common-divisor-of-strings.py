class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        a, b = (str1, str2) if len(str1) >= len(str2) else (str2, str1)
        res = ""
        for i in range(1, len(b) + 1):
            if int(len(a) / i) * b[:i:] == a and int(len(b) / i) * b[:i:] == b:
                res = b[:i:]
        return res