class Solution {
public:
    int longestPalindrome(vector<string>& words) {
        int mat[26][26] = {0};
        for(int i = 0; i < words.size(); ++i) {
            ++mat[(int) words[i][0] - 'a'][(int) words[i][1] - 'a'];
        }
        int res = 0;
        for(int i = 0; i < 26; ++i) {
            for(int j = 0; j < i; ++j) {
                res += 4 * min(mat[i][j], mat[j][i]);
            }
        }
        bool middle = false;
        for(int i = 0; i < 26; ++i) {
            if(not middle and mat[i][i] % 2 == 1) {
                res += 2;
                middle = true;
            }
            res += 4 * ((int) mat[i][i] / 2);
        }
        return res;
    }
};