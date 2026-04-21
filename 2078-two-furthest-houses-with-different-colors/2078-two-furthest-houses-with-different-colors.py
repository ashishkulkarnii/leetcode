class Solution:
    def maxDistance(self, colors: List[int]) -> int:
        i = 0
        n = len(colors)
        res = 0
        while n - i > res:
            j = n - 1
            while j - i > res:
                if colors[i] != colors[j]:
                    res = j - i
                    break
                else:
                    j -= 1
            i += 1
        return res