class Solution {
public:
    bool isToeplitzMatrix(vector<vector<int>>& matrix) {
        int temp, i, j;
        for(int row = matrix.size() - 1; row >= 0; --row) {
            temp = matrix[row][0];
            i = row; j = 0;
            while(i < matrix.size() and i >= 0 and j < matrix[0].size() and j >= 0) {
                if(temp != matrix[i][j]) {
                    return false;
                }
                ++i; ++j;
            }
        }
        for(int col = 0; col < matrix[0].size(); ++col) {
            temp = matrix[0][col];
            i = 0; j = col;
            while(i < matrix.size() and i >= 0 and j < matrix[0].size() and j >= 0) {
                if(temp != matrix[i][j]) {
                    return false;
                }
                ++i; ++j;
            }
        }
        return true;
    }
};