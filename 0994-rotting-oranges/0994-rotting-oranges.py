class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        minute = 0
        m = len(grid[0])
        n = len(grid)
        rots = []
        for i in range(m):
            for j in range(n):
                if grid[j][i] == 2:
                    rots.append([i, j])
        def spread():
            change = False
            for x in range(len(rots)):
                i, j = rots[x]
                if i > 0 and grid[j][i-1] == 1:
                    grid[j][i-1] = 2
                    rots.append([i - 1, j])
                    change = True
                if i < m - 1 and grid[j][i+1] == 1:
                    grid[j][i+1] = 2
                    rots.append([i + 1, j])
                    change = True
                if j > 0 and grid[j-1][i] == 1:
                    grid[j-1][i] = 2
                    rots.append([i, j - 1])
                    change = True
                if j < n - 1 and grid[j+1][i] == 1:
                    grid[j+1][i] = 2
                    rots.append([i, j + 1])
                    change = True
            return change
        while spread():
            minute += 1
        for row in grid:
            for orange in row:
                if orange == 1:
                    return -1
        return minute