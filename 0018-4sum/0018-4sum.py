class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        n = len(nums)
        seen = set()
        result = set()
        for i in range(n):
            for j in range(i + 1, n):
                for k in range(j + 1, n):
                    required = target - nums[i] - nums[j] - nums[k]
                    if required in seen:
                        result.add(tuple(sorted([required, nums[i], nums[j], nums[k]])))
            seen.add(nums[i])
        return result