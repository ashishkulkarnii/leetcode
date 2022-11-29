class RandomizedSet:

    def __init__(self):
        self.myset = set()

    def insert(self, val: int) -> bool:
        if val in self.myset:
            return False
        self.myset.add(val)
        return True

    def remove(self, val: int) -> bool:
        if val in self.myset:
            self.myset.remove(val)
            return True
        return False

    def getRandom(self) -> int:
        return random.choice(tuple(self.myset))


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()