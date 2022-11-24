class Solution {
public:
    vector<vector<char>> board;
    string word;
    int wordlength, n, m;
    bool dfs(int i, int j, int depth) {
        if(depth == wordlength) {
            return true;
        }
        if(i < 0 or j < 0 or i >= n or j >= m or board[i][j] != word[depth]) {
            return false;
        }
        board[i][j] = '.';
        bool res = dfs(i+1, j, depth+1) or dfs(i-1, j, depth+1) or dfs(i, j+1, depth+1) or dfs(i, j-1, depth+1);
        board[i][j] = word[depth];
        return res;
    }
    bool exist(vector<vector<char>>& board1, string word1) {
        word = word1;
        board = board1;
        wordlength = word.length();
        n = board.size();
        m = board[0].size();
        for(int i = 0; i < n; ++i) {
            for(int j = 0; j < m; ++j) {
                if(dfs(i, j, 0)) {
                    return true;
                }
            }
        }
        return false;
    }
};