class Solution {
public:
    int minPathSum(vector<vector<int>>& grid) {
        int m = grid.size(), n = grid[0].size();
        for(int row = 0; row < m; row++) {
            for(int col = 0; col < n; col++) {
                if(row == 0) {
                    if(col != 0) {
                        grid[row][col] += grid[row][col-1];
                    }
                }
                else {
                    if(col != 0) {
                        grid[row][col] += min(grid[row-1][col], grid[row][col-1]);
                    }
                    else {
                        grid[row][col] += grid[row-1][col];
                    }
                }
            }
        }
        return grid[m-1][n-1];
    }
};