class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        earth = 'abcdefghijklmnopqrstuvwxyz'
        alien_to_earth = dict(zip(order, earth))
        for i in range(len(words)):
            word = list(words[i])
            for j in range(len(word)):
                word[j] = alien_to_earth[word[j]]
            words[i] = ''.join(word)
        if words == sorted(words):
            return True
        return False