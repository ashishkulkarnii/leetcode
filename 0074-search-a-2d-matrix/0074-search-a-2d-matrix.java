class Solution {
    public boolean searchMatrix(int[][] matrix, int target) {
        int rows = matrix.length, cols = matrix[0].length;
        // find row
        int high = rows - 1, low = 0, mid, row = -1;
        while(high >= low) {
            mid = (high + low) / 2;
            if(matrix[mid][0] == target)
                return true;
            else if(matrix[mid][0] < target) {
                row = mid;
                low = mid + 1;
            }
            else
                high = mid - 1;
        }
        if(row < 0)
            return false;
        // find column
        int col = -1; high = cols - 1; low = 0;
        while(high >= low) {
            mid = (high + low) / 2;
            if(matrix[row][mid] == target)
                return true;
            else if(matrix[row][mid] < target)
                low = mid + 1;
            else
                high = mid - 1;
        }
        return false;
    }
}