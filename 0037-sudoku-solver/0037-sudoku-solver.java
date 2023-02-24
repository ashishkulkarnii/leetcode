class Solution {
    private boolean isValid(char[][] board, int row, int col, char c) {
        for(int i = 0; i < 9; ++i) {
            if(board[row][i] != '.' && board[row][i] == c)
                return false;
            if(board[i][col] != '.' && board[i][col] == c)
                return false;
            if(board[3 * (row / 3) + i / 3][3 * (col / 3) + i % 3] != '.' && board[3 * (row / 3) + i / 3][3 * (col / 3) + i % 3] == c)
                return false;
        }
        return true;
    }
    private boolean solve(char[][] board) {
        for(int x = 0; x < 9; ++x) {
            for(int y = 0; y < 9; ++y) {
                if(board[y][x] == '.') {
                    for(char c = '1'; c <= '9'; ++c) {
                        if(isValid(board, y, x, c)) {
                            board[y][x] = c;
                            if(solve(board))
                                return true;
                            else
                                board[y][x] = '.';
                        }
                    }
                    return false;
                }
            }
        }
        return true;
    }
    public void solveSudoku(char[][] board) {
        solve(board);
    }
}