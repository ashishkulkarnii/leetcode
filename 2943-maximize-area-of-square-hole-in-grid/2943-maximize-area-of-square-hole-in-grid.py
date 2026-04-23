class Solution:
    def maximizeSquareHoleArea(self, n: int, m: int, hBars: List[int], vBars: List[int]) -> int:
        def len_longest_continuous(arr):
            arr.sort()
            l = 0
            temp = 1
            for i, b in enumerate(arr):
                if i > 0 and b == 1 + arr[i-1]:
                    temp += 1
                else:
                    l = max(l, temp)
                    temp = 1
            return max(l, temp)
        x, y = len_longest_continuous(vBars), len_longest_continuous(hBars) 
        dim = min(x, y) + 1
        return dim ** 2
