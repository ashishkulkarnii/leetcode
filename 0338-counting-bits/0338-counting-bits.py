class Solution:
    @staticmethod
    def bitsInNum(n: int) -> int:
        bits = 0
        while n:
            bits += n % 2
            n //= 2
        return bits

    def countBits(self, n: int) -> List[int]:
        bits = []
        for i in range(n + 1):
            bits.append(Solution.bitsInNum(i))
        return bits