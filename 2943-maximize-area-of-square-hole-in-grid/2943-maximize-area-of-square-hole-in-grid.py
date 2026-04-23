class Solution:
    def maximizeSquareHoleArea(self, n: int, m: int, hBars: List[int], vBars: List[int]) -> int:
        hBars.sort()
        vBars.sort()
        print(hBars)
        x = 0
        temp = 1
        for i, b in enumerate(vBars):
            if i > 0 and b == 1 + vBars[i-1]:
                temp += 1
            else:
                x = max(x, temp)
                temp = 1
        x = max(x, temp)
        y = 0
        temp = 1
        for i, b in enumerate(hBars):
            if i > 0 and b == 1 + hBars[i-1]:
                temp += 1
            else:
                y = max(y, temp)
                temp = 1
        y = max(y, temp)
        dim = min(x, y) + 1
        return dim ** 2
