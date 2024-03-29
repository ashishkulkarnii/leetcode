import numpy as np

class Solution:
    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
        N = len(grid)
        res = 0

        grid = np.array(grid)
        ns = np.array([0] * N)
        ew = np.array([0] * N)

        for i in range(N):
            ns[i] = max(grid[:, i])
            ew[i] = max(grid[i, :])

        for x in range(N):
            for y in range(N):
                curr_max = min(ns[x], ew[y])
                res += curr_max - grid[y, x]

        return res
