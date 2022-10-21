class Solution {
public:
    bool searchMatrix(vector<vector<int>>& matrix, int target) {
        int b = 0, e = matrix.size() - 1, m;
        while(e >= b) {
            m = (b + e) / 2;
            if(matrix[m][0] == target) {
                return true;
            }
            else if(matrix[m][0] > target) {
                e = m - 1;
            }
            else {
                b = m + 1;
            }
        }
        m = (b + e) / 2;
        cout<<m;
        b = 0;
        e = matrix[m].size() - 1;
        int m2;
        while(b <= e) {
            m2 = (b + e) / 2;
            if(matrix[m][m2] == target) {
                return true;
            }
            else if(matrix[m][m2] < target) {
                b = m2 + 1;
            }
            else {
                e = m2 - 1;
            }
        }
        return false;
    }
};