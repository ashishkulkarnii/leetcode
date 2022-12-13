class Solution {
public:
    int minFallingPathSum(vector<vector<int>>& matrix) {
        for(int row = 1; row < matrix.size(); ++row) {
            for(int col = 0; col < matrix[0].size(); ++col) {
                if(col == 0 or col == matrix[0].size() - 1) {
                    if(col == 0 and col == matrix[0].size() - 1) {
                        matrix[row][col] += matrix[row-1][col];
                    }
                    else if(col == 0) {
                        matrix[row][col] += min(matrix[row-1][col], matrix[row-1][col+1]);
                    }
                    else {
                        matrix[row][col] += min(matrix[row-1][col], matrix[row-1][col-1]);
                    }
                }
                else {
                    matrix[row][col] += min({matrix[row-1][col-1], matrix[row-1][col], matrix[row-1][col+1]});
                }
            }
        }
        return *min_element(matrix[matrix.size()-1].begin(), matrix[matrix.size()-1].end());
    }
};