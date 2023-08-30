class Solution:
    def minimumReplacement(self, nums: List[int]) -> int:
        steps = 0
        prev = nums[-1]
        for num in reversed(nums[:-1]):
            if num > prev:
                divs = (num + prev - 1) // prev
                prev = num // divs
                steps += divs - 1
            else:
                prev = num
        return steps