class Solution:
    def rev(self, s):
        return s[::-1]
    def reverseWords(self, s: str) -> str:
        return ' '.join(map(self.rev, s.split()))