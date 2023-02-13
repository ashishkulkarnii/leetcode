class Solution {
public:
    int uniquePaths(int m, int n) {
        vector<int> row(n, 1);
        for(int y = 1; y < m; ++y) {
            for(int x = 1; x < n; ++x) {
                row[x] += row[x-1];
            }
        }
        return row[n-1];
    }
};