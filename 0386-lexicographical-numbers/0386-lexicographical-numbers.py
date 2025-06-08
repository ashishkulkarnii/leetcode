class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        return [int(x) for x in sorted([str(x) for x in range(1, n + 1)])]