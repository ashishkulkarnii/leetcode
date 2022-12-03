class Solution:
    def frequencySort(self, s: str) -> str:
        return ''.join([i[1] * i[0] for i in Counter(s).most_common()])