class Solution:
    def makeGood(self, s: str) -> str:
        i = 0
        s = list(s)
        while i <= len(s) - 2:
            if abs(ord(s[i]) - ord(s[i+1])) == ord('a') - ord('A'):
                s = s[:i:] + s[i+2::]
                i = max(-1, i-2)
            i += 1
        return ''.join(s)