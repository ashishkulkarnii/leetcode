class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        return sorted(sorted(list(set(words))), key = lambda x: words.count(x), reverse = True)[:k:]