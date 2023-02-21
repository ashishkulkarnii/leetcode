class Solution:
    def firstBadVersion(self, n: int) -> int:
        b = 1
        e = n
        while b < e:
            n = int((b + e) / 2)
            if isBadVersion(n):
                e = n - 1
            else:
                b = n + 1
        n -= 1
        while(not isBadVersion(n)):
            n += 1
        return n