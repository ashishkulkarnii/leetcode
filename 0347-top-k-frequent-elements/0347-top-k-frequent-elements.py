class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq_nums = collections.defaultdict(set)
        num_freqs = collections.defaultdict(int)
        for n in nums:
            freq_nums[num_freqs[n]].discard(n)
            num_freqs[n] += 1
            freq_nums[num_freqs[n]].add(n)
        res = []
        for ns in list(freq_nums.values())[::-1]:
            if k:
                res.extend(ns)
            else:
                return res
            k -= len(ns)
        