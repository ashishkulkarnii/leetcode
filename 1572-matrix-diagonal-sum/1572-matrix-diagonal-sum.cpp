class Solution {
public:
    int diagonalSum(vector<vector<int>>& mat) {
        int n = mat.size(), res = 0;
        for(int row = 0; row < n; ++row) {
            int col = row;
            res += mat[row][col];
        }
        for(int row = 0; row < n; ++row) {
            int col = n - row - 1;
            if(row != col)
                res += mat[row][col];
        }
        return res;
    }
};