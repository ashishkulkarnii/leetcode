class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix) - 1
        for x in range(0, int((n + 1) / 2)):
            for y in range(x, n - x):
                temp = matrix[y][x]
                matrix[y][x] = matrix[n - x][y]
                matrix[n - x][y] = matrix[n - y][n - x]
                matrix[n - y][n - x] = matrix[x][n - y]
                matrix[x][n - y] = temp
                print(matrix)
