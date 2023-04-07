class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        queue = set([(x, 0) for x in range(0, len(grid[0]))] + [(x, len(grid) - 1) for x in range(0, len(grid[0]))] + [(0, y) for y in range(0, len(grid))] + [(len(grid[0]) - 1, y) for y in range(0, len(grid))])
        visited = set()
        while queue:
            x, y = queue.pop()
            if grid[y][x] == 1 and (x, y) not in visited:
                visited.add((x, y))
                if y > 0:
                    queue.add((x, y - 1))
                if y < len(grid) - 1:
                    queue.add((x, y + 1))
                if x > 0:
                    queue.add((x - 1, y))
                if x < len(grid[0]) - 1:
                    queue.add((x + 1, y))
        ans = 0
        for y, row in enumerate(grid):
            for x, val in enumerate(row):
                if val == 1 and (x, y) not in visited:
                    ans += 1
        return ans