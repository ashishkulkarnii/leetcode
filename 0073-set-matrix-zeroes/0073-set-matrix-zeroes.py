class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        rows = len(matrix) * [1]
        cols = len(matrix[0]) * [1]
        for row in range(len(matrix)):
            for col in range(len(matrix[0])):
                if matrix[row][col] == 0:
                    rows[row] = 0
                    cols[col] = 0
                    continue
        for row in range(len(matrix)):
            for col in range(len(matrix[0])):
                if rows[row] == 0 or cols[col] == 0:
                    matrix[row][col] = 0