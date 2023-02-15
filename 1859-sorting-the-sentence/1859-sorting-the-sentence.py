class Solution:
    def sortSentence(self, s: str) -> str:
        return ' '.join([w[:-1:] for w in sorted(s.split(), key=lambda w: w[-1])])