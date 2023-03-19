class WordDictionary:

    def __init__(self):
        self.words = defaultdict(set)

    def addWord(self, word: str) -> None:
        self.words[len(word)].add(word)

    def search(self, word: str) -> bool:
        if '.' in word:
            words = self.words[len(word)]
            for w in words:
                if all(word[i] in {w[i], '.'} for i in range(len(word))):
                    return True
            return False
        return word in self.words[len(word)]

# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)