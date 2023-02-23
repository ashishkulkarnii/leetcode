class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        cp = sorted(list(zip(capital, profits)), reverse=True)
        q = []
        for _ in range(k):
            for i, (c, p) in enumerate(cp):
                if c <= w:
                    bisect.insort(q, p)
                    cp.pop(i)
            if not q:
                break
            w += q.pop(-1)
        return w