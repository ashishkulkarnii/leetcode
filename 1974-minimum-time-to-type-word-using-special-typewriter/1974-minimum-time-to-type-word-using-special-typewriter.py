class Solution:
    def minTimeToType(self, word: str) -> int:
        return sum([min(abs(ord(word[i]) - ord(word[i+1])), 26 - abs(ord(word[i]) - ord(word[i+1]))) for i in range(0, len(word)-1)]) + len(word) + min(abs(ord('a') - ord(word[0])), 26 - abs(ord('a') - ord(word[0])))