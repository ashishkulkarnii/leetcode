class Solution:
    def mostFrequentEven(self, nums: List[int]) -> int:
        counter = collections.defaultdict(int)
        for n in nums:
            if not n % 2:
                counter[n] += 1
        if not counter:
            return -1
        pairs = [(freq, num) for num, freq in counter.items()]
        pairs.sort(key=lambda pair: (-pair[0], pair[1])) 
        return pairs[0][1]