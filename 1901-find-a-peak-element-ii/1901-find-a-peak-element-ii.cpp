class Solution {
public:
    vector<int> findPeakGrid(vector<vector<int>>& mat) {
        vector<int> res = {0, 0};
        for(int row = 0; row < mat.size(); ++row) {
            for(int col = 0; col < mat[row].size(); ++col) {
                if(col == 0 and row == 0) continue;
                if(col != 0) if(mat[row][col] <= mat[row][col-1]) continue;
                if(col != mat[0].size() - 1) if(mat[row][col] <= mat[row][col+1]) continue;
                if(row != 0) if(mat[row][col] <= mat[row-1][col]) continue;
                if(row != mat.size() - 1) if(mat[row][col] <= mat[row+1][col]) continue;
                res[0] = row; res[1] = col;
            }
        }
        return res;
    }
};