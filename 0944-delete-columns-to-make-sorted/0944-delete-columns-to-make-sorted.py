class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        res = 0
        columns = [list(x) for x in zip(*strs)]
        for index, column in enumerate(columns):
            if sorted(column) != column:
                res += 1
        return res