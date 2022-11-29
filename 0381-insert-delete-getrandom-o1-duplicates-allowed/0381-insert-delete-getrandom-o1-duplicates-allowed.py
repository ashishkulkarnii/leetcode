class RandomizedCollection:

    def __init__(self):
        self.nums = dict()
        self.list_nums = list()

    def insert(self, val: int) -> bool:
        self.list_nums.append(val)
        if val in self.nums:
            self.nums[val] += 1
            return False
        self.nums[val] = 1
        return True

    def remove(self, val: int) -> bool:
        if val in self.nums:
            self.list_nums.remove(val)
            self.nums[val] -= 1
            if self.nums[val] <= 0:
                del self.nums[val]
            return True
        return False

    def getRandom(self) -> int:
        return random.choice(self.list_nums)



# Your RandomizedCollection object will be instantiated and called as such:
# obj = RandomizedCollection()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()