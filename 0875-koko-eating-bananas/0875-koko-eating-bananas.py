class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        low = 1
        high = max(piles)
        def sim(k):
            return sum(math.ceil(p / k) for p in piles)
        k = high
        while low <= high:
            k_ = (low + high) // 2
            h_ = sim(k_)
            if h_ <= h:
                k = min(k, k_)
                high = k_ - 1
            else:
                low = k_ + 1
        return k