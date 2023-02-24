class Solution:
    def minimumDeviation(self, nums: List[int]) -> int:
        for i, n in enumerate(nums):
            if nums[i] % 2 == 1:
                nums[i] *= 2
        nums = list(set(nums))
        heap = []
        for n in nums:
            bisect.insort(heap, n)
        min_dev = heap[-1] - heap[0]
        while min_dev:
            curr = heap.pop(-1)
            if curr % 2 == 0:
                curr //= 2
                bisect.insort(heap, curr)
            else:
                break
            min_dev = min(min_dev, heap[-1] - heap[0])
        return min_dev
