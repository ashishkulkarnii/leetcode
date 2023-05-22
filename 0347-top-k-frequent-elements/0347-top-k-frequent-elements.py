from bisect import insort

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        fns = []
        for num, freq in Counter(nums).items():
            insort(fns, [-freq, num])
        return [n for f, n in fns[:k:]]