class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        m, n = len(maze), len(maze[0])
        dir = [[-1, 0], [1, 0], [0, -1], [0, 1]]
        qu = []
        qu.append([entrance])
        i, j = entrance
        maze[i][j] = '..'
        while True:
            curr_level = qu[-1]
            next_level = []
            for i, j in curr_level:
                for x, y in dir:
                    if 0 <= i+x < m and 0 <= j+y < n and maze[i+x][y+j] == '.':
                        if i+x == 0 or i+x == m-1 or j+y == 0 or j+y == n-1:
                            return len(qu)
                        maze[i+x][y+j] = '..'
                        next_level.append([i+x, y+j])
            if len(next_level):
                qu.append(next_level)
            else:
                return -1
