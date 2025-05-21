class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        zr = set()
        zc = set()
        m = len(matrix)
        n = len(matrix[0])
        for row in range(m):
            for col in range(n):
                if matrix[row][col] == 0:
                    zr.add(row)
                    zc.add(col)
        for row in range(m):
            if row in zr:
                matrix[row] = [0] * n
            else:
                matrix[row] = [0 if i in zc else x for i, x in enumerate(matrix[row])]
        