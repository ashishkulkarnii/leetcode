def convert(x, y, n):
    """Returns x and y"""
    return y, n - x - 1

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        for i in range(0, n - 1):
            for j in range(i, n - 1 - i):
                x, y = i, j
                temp = matrix[i][j]
                for _ in range(4):
                    newx, newy = convert(x, y, n)
                    newtemp = matrix[newx][newy]
                    matrix[newx][newy] = temp
                    x, y, temp = newx, newy, newtemp
        
