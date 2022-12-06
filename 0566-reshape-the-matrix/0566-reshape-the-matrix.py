class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        if len(mat) * len(mat[0]) != r * c:
            return mat
        temp = []
        for row in mat:
            for num in row:
                temp.append(num)
        res = []
        for i in range(r):
            t = []
            for j in range(c):
                t.append(temp[0])
                temp.pop(0)
            res.append(t)
        return res