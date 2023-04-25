class SmallestInfiniteSet:

    def __init__(self):
        self.removed = set()

    def popSmallest(self) -> int:
        res = 1
        while res in self.removed:
            res += 1
        self.removed.add(res)
        return res
    
    def addBack(self, num: int) -> None:
        self.removed.discard(num)


# Your SmallestInfiniteSet object will be instantiated and called as such:
# obj = SmallestInfiniteSet()
# param_1 = obj.popSmallest()
# obj.addBack(num)