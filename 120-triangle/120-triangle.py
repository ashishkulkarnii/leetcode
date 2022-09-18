class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        for i in range(1, len(triangle)):
            for j in range(len(triangle[i])):
                if j == 0:
                    triangle[i][j] += triangle[i-1][0]
                elif j == len(triangle[i]) - 1:
                    triangle[i][j] += triangle[i-1][len(triangle[i-1]) - 1]
                else:
                    t1 = triangle[i-1][j-1]
                    t2 = triangle[i-1][j]
                    triangle[i][j] += min([t1,t2])
        return(min(triangle[-1]))