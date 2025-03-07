class Solution:
    def closestPrimes(self, left: int, right: int) -> List[int]:
        n = 10 ** 6
        sieve = [True for _ in range(n + 1)]
        sieve[1] = False
        p = 2
        while p ** 2 < n:
            if sieve[p]:
                for i in range(2 * p, n + 1, p):
                    sieve[i] = False
            p += 1
        smallest_gap = n
        pair = [-1, -1]
        fp = -1
        for i, isp in list(enumerate(sieve))[left:right+1]:
            if isp:
                if fp != -1 and i - fp < smallest_gap:
                    smallest_gap = i - fp
                    pair = [fp, i]
                fp = i
        return pair
