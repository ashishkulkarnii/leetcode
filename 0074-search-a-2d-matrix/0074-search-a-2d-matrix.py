class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        beg, end = 0, len(matrix) - 1
        mid = (beg + end) // 2
        while beg < end:
            if matrix[mid][0] <= target <= matrix[mid][-1]:
                break
            elif matrix[mid][0] > target:
                end = mid - 1
            else:
                beg = mid + 1
            mid = (beg + end) // 2
        row = matrix[mid]
        beg, end = 0, len(row) - 1
        mid = (beg + end) // 2
        while beg <= end:
            if row[mid] < target:
                beg = mid + 1
            elif row[mid] > target:
                end = mid - 1
            else:
                return True
            mid = (beg + end) // 2
        return False