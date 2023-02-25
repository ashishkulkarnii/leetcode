class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def dfs(r, c, color):
            if grid[r][c] == '1':
                grid[r][c] = color
                if r > 0:
                    dfs(r - 1, c, color)
                if r < len(grid) - 1:
                    dfs(r + 1, c, color)
                if c > 0:
                    dfs(r, c - 1, color)
                if c < len(grid[0]) - 1:
                    dfs(r, c + 1, color)
        
        colour = 2
        for x in range(len(grid[0])):
            for y in range(len(grid)):
                if grid[y][x] == '1':
                    colour += 1
                    dfs(y, x, colour)
        print(grid)
        return colour - 2