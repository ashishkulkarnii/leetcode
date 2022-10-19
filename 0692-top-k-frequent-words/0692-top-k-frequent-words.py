class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        unique_words = sorted(list(set(words)))
        return sorted(unique_words, key = lambda x: words.count(x), reverse = True)[:k:]