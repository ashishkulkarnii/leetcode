class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        largest = [-math.inf, -math.inf]
        index = -1
        for i, n in enumerate(nums):
            if n > largest[1]:
                largest[0], largest[1] = largest[1], n
                index = i
            elif n > largest[0]:
                largest[0] = n
        return index if largest[0] * 2 <= largest[1] else -1