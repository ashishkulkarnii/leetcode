class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        a = set()
        for c in sentence:
            a.add(c)
            if len(a) == 26: return True
        return len(a) == 26