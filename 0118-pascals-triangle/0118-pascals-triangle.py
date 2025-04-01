class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        rows = [[1]]
        prev = rows[-1]
        for _ in range(numRows - 1):
            row = [1]
            for i, n in enumerate(prev[:-1]):
                row.append(n + prev[i+1])
            row.append(1)
            rows.append(row)
            prev = row
        return rows