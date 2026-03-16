class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m = len(grid[0])
        n = len(grid)
        i, j = 0, 0
        color = 0
        def bfs(i, j, color):
            if 0 <= i < m and 0 <= j < n and grid[j][i] == "1":
                grid[j][i] = color
                bfs(i + 1, j, color)
                bfs(i - 1, j, color)
                bfs(i, j + 1, color)
                bfs(i, j - 1, color)
        while i < m and j < n:
            if grid[j][i] == "1":
                bfs(i, j, color)
                color += 1
            else:
                i += 1
                if i == m:
                    i = 0
                    j += 1
        return color