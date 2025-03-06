class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        n = len(grid)
        sieve = [False for i in range(1, n * n + 1)]
        missing, repeated = -1, -1
        for y in range(n):
            for x in range(n):
                if sieve[grid[y][x] - 1]:
                    repeated = grid[y][x]
                else:
                    sieve[grid[y][x] - 1] = True
        missing = sieve.index(False) + 1
        return [repeated, missing]