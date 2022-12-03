class Solution:
    def frequencySort(self, s: str) -> str:
        return ''.join([frequency * character for character, frequency in Counter(s).most_common()])