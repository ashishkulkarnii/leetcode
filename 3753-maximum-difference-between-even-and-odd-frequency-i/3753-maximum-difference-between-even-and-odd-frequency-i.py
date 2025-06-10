class Solution:
    def maxDifference(self, s: str) -> int:
        freqs = [0] * 26
        for c in s:
            freqs[ord(c) - ord('a')] += 1
        maxodd = -1
        mineve = len(s) + 1
        for i in range(26):
            if freqs[i] % 2:
                maxodd = max(maxodd, freqs[i])
            elif freqs[i] > 0:
                mineve = min(mineve, freqs[i])
        return maxodd - mineve