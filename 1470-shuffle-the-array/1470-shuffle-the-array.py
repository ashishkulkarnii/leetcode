class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        return [i for t in zip(nums[:n], nums[n:]) for i in t]