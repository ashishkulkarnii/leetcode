class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        return set(word1) == set(word2) and sorted([word1.count(i) for i in list(set(word1))]) == sorted([word2.count(i) for i in list(set(word2))])