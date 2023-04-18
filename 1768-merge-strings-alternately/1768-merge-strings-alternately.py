class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        result = []
        word1, word2 = list(word1), list(word2)
        while word1 and word2:
            result += [word1.pop(0), word2.pop(0)]
        return ''.join(result + word1 + word2)