class Solution:
    def sumZero(self, n: int) -> List[int]:
        return [y for x in range(1, n // 2 + 1) for y in (x, -x)] + [0] * (n % 2)