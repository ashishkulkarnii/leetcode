class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        codes = set()
        n_codes = 2 ** k
        for i in range(len(s) - k + 1):
            codes.add(s[i:i+k])
            if len(codes) == n_codes:
                return True
        return False