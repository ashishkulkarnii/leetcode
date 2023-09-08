class Solution {
public:
    vector<vector<int>> generate(int numRows) {
        vector<vector<int>> result = {{1}};
        vector<int>temp;
        for(int i = 2; i < numRows + 1; i++) {
            temp.clear();
            for(int j = 0; j < i; j++) {
                if(j == 0 or j == i-1) {
                    temp.push_back(1);
                }
                else {
                    temp.push_back(result[i-2][j-1] + result[i-2][j]);
                }
            }
            result.push_back(temp);
        }
        return result;
    }
};