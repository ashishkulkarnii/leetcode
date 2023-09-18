class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        return sorted(list(range(len(mat))), key=lambda x: mat[x].count(1))[:k]
