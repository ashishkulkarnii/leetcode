class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        pq = []
        c = collections.Counter(nums)
        for num, freq in c.items():
            heapq.heappush(pq, (-freq, num))
        res = []
        for i in range(k):
            res.append(heapq.heappop(pq)[1])
        return res