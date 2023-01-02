class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        return word.capitalize() == word or word.upper() == word or word.lower() == word