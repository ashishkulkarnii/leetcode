class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        return [i + len(list(filter(lambda x: x < target, nums))) for i in range(nums.count(target))]