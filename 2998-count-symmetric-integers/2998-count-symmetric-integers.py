class Solution:
    def countSymmetricIntegers(self, low: int, high: int) -> int:
        def is_symm(n):
            n = str(n)
            if len(n) % 2:
                return False
            l, r = n[:len(n)//2], n[len(n)//2:]
            def sums(s):
                return sum([int(c) for c in list(s)])
            return sums(l) == sums(r)
        res = 0
        for n in range(low, high + 1):
            res += is_symm(n)
        return res