class Solution:
    def maxMatrixSum(self, matrix: List[List[int]]) -> int:
        num_neg = 0
        min_num = float('inf')
        sum_pos = 0
        for row in matrix:
            for num in row:
                if num < 0:
                    num_neg += 1
                min_num = min(min_num, abs(num))
                sum_pos += abs(num)
        if num_neg % 2:
            return sum_pos - 2 * abs(min_num)
        return sum_pos