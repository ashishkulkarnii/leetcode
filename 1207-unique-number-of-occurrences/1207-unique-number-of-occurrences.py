class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        nums = dict()
        for n in arr:
            if n in nums.keys():
                nums[n] += 1
            else:
                nums[n] = 1
        return len(nums.values()) == len(set(nums.values()))