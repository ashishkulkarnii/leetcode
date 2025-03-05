class Solution:
    def rotateTheBox(self, boxGrid: List[List[str]]) -> List[List[str]]:
        box = ["".join(row) for row in boxGrid]
        for i, row in enumerate(box):
            while "#." in row:
                row = row.replace("#.", ".#")
            box[i] = row
        t_box = [[""] * len(box) for _ in range(len(box[0]))]
        for i in range(len(box)):
            for j in range(len(box[0])):
                t_box[j][len(box)-i-1] = box[i][j]
        return t_box