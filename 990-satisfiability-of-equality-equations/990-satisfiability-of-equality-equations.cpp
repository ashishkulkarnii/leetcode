class Solution {
public:
    bool equationsPossible(vector<string>& equations) {
        int arr[26][26] = {0};
        for(int i = 0; i < equations.size(); i++) {
            if(equations[i][1] == '=') {
                arr[(int) equations[i][0] - 97][(int) equations[i][3] - 97] = 1;
                arr[(int) equations[i][3] - 97][(int) equations[i][0] - 97] = 1;
            }
        }
        for(int i = 0; i < 26; i++) {
            for(int j = 0; j < 26; j++) {
                for(int k = 0; k < 26; k++) {
                    if(arr[i][j] == 1 and arr[j][k] == 1) {
                        arr[i][k] = 1;
                        arr[k][i] = 1;
                    }
                }
            }
        }
        for(int i = 0; i < equations.size(); i++) {
            if(equations[i][1] == '!') {
                if(equations[i][0] == equations[i][3] or arr[(int) equations[i][0] - 97][(int) equations[i][3] - 97] == 1) {
                    return false;
                }
            }
        }
        return true;
    }
};