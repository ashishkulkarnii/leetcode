class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        return [nums[i//2+n] if i % 2 else nums[i//2] for i in range(n * 2)]