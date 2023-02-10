class Solution:
    def nextToLand(self, grid, point):
        x, y = point
        n = len(grid)
        if grid[y][x] == 1:
            return False
        else:
            if x > 0 and grid[y][x-1]:
                return True
            elif y > 0 and grid[y-1][x]:
                return True
            # elif x > 0 and y > 0 and grid[y-1][x-1]:
            #     return True
            elif x < n - 1 and grid[y][x+1]:
                return True
            elif y < n - 1 and grid[y+1][x]:
                return True
            # elif x < n - 1 and y < n - 1 and grid[y+1][x+1]:
            #     return True
            else:
                return False
    def maxDistance(self, grid: List[List[int]]) -> int:
        n = len(grid)
        not_visited = set()
        for i in range(n):
            for j in range(n):
                if grid[j][i] != 1:
                    not_visited.add((i, j))
        if len(not_visited) == n * n or len(not_visited) == 0:
            return -1
        res = 0
        while len(not_visited) > 0:
            temp = []
            for y in range(n):
                for x in range(n):
                    if not grid[y][x] and self.nextToLand(grid, (x, y)):
                        temp.append((x, y))
                        not_visited.discard((x, y))
            for x, y in temp:
                grid[y][x] = 1
            res += 1
        return res