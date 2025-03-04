class Solution:
    def checkPowersOfThree(self, n: int) -> bool:
        while n > 0:
            if n % 3 == 0:
                n //= 3
                continue
            
            if (n - 1) % 3 == 0:
                n = (n - 1) // 3
                continue
            
            return False
        return True