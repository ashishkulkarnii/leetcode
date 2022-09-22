class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for y, row in enumerate(board):
            for x in range(len(row)):
                if row[x] != '.':
                    temp = row[x]
                    row[x] = '.'
                    
                    # check row
                    if temp in row:
                        return False
                    
                    # check column
                    for rows in board:
                        if rows[x] == temp:
                            return False;
                    
                    # check 3x3
                    i = 3 * int(x/3)
                    j = 3 * int(y/3)
                    for xt in range(i, i+3):
                        for yt in range(j, j+3):
                            if board[yt][xt] == temp:
                                return False
                    
                    row[x] = temp;
        return True