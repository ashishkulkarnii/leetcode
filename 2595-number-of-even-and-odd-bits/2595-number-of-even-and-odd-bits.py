class Solution:
    def evenOddBit(self, n: int) -> List[int]:
        ans = [0, 0]
        i = False
        while n > 0:
            if n % 2:
                ans[i] += 1
            i = not i
            n //= 2
        return ans
