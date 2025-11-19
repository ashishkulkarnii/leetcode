class FindSumPairs:

    def __init__(self, nums1: List[int], nums2: List[int]):
        self.n1 = nums1
        self.n2 = nums2
        self.c2 = collections.Counter(nums2)

    def add(self, index: int, val: int) -> None:
        self.c2[self.n2[index]] -= 1
        self.n2[index] += val
        self.c2[self.n2[index]] += 1

    def count(self, tot: int) -> int:
        return sum(self.c2[tot-i] for i in self.n1)



# Your FindSumPairs object will be instantiated and called as such:
# obj = FindSumPairs(nums1, nums2)
# obj.add(index,val)
# param_2 = obj.count(tot)