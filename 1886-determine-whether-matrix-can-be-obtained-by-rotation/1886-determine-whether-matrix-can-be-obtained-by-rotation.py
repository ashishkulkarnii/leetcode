def compare(a, b):
        for i in range(len(a)):
            for j in range(len(a)):
                if a[i][j] != b[i][j]:
                    return False
        return True
    
def rotate90(matrix):
        n = len(matrix) - 1
        for x in range(0, int((n + 1) / 2)):
            for y in range(x, n - x):
                temp = matrix[y][x]
                matrix[y][x] = matrix[n - x][y]
                matrix[n - x][y] = matrix[n - y][n - x]
                matrix[n - y][n - x] = matrix[x][n - y]
                matrix[x][n - y] = temp

class Solution:
    def findRotation(self, mat: List[List[int]], target: List[List[int]]) -> bool:
        if len(mat) != len(target) or len(mat[0]) != len(target[0]) or len(mat) != len(mat[0]) or len(target) != len(target[0]):
            return False
        if compare(mat, target):
            return True
        rotate90(target)
        if compare(mat, target):
            return True
        rotate90(target)
        if compare(mat, target):
            return True
        rotate90(target)
        if compare(mat, target):
            return True
        return False
        
        