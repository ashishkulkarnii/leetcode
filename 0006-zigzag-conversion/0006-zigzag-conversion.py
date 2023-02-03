class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        
        ans = [[] for i in range(numRows)]
        i = 0
        row = 0
        down = True
        
        while i < len(s):
            if row == numRows:
                row -= 2
                down = False
                continue
            if row == -1:
                row += 2
                down = True
                continue
            ans[row].append(s[i])
            i += 1
            row += 1 if down else -1
        
        res = ""
        for i in ans:
            for j in i:
                res += j
                
        return res