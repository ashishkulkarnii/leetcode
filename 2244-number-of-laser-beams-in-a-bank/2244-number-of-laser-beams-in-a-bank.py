class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        r1 = 0
        r2 = 1
        beams = 0
        while r2 < len(bank):
            if (d1 := bank[r1].count("1")) == 0:
                r1 += 1
                r2 = r1 + 1
            elif (d2 := bank[r2].count("1")) == 0:
                r2 += 1
            else:
                beams += d1 * d2
                r1 += 1
                r2 = r1 + 1
        return beams