class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        return set(list(word1)) == set(list(word2)) and sorted([word1.count(i) for i in list(set(list(word1)))]) == sorted([word2.count(i) for i in list(set(list(word2)))])