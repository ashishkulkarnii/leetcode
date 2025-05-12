class Solution:
    def findEvenNumbers(self, digits: List[int]) -> List[int]:
        n = int("".join([str(i) for i in sorted(digits, reverse=True)]))
        c = collections.Counter(digits)
        res = []
        for i in range(100, 999, 2):
            subc = collections.Counter(str(i))
            good = True
            for d, f in subc.items():
                if c.get(int(d), 0) < f:
                    good = False
            if good:
                res.append(i)
        return res