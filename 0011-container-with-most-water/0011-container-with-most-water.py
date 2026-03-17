class Solution:
    def maxArea(self, height: List[int]) -> int:
        n = len(height)
        i, j = 0, n - 1
        water = 0
        while i <= j:
            water = max(water, min(height[i],  height[j]) * (j - i))
            if height[i] > height[j]:
                j -= 1
            elif height[i] < height[j]:
                i += 1
            else:
                i += 1
                j -= 1
        return water
