class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        unique_words = list(set(words))
        unique_words.sort()
        unique_words.sort(key = lambda x: words.count(x), reverse = True)
        return unique_words[:k:]