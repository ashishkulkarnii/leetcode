class Solution:
    def isThree(self, n: int) -> bool:
        return sum([1 if n % i == 0 else 0 for i in range(1, n+1)]) == 3
                