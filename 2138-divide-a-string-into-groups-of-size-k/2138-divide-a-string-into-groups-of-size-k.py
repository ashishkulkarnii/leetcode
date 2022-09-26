class Solution:
    def divideString(self, s: str, k: int, fill: str) -> List[str]:
        while len(s) % k: s += fill[0]
        return [s[p:p+k] for p in range(0, len(s), k)]