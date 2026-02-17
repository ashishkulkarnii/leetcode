class Solution:
    def readBinaryWatch(self, turnedOn: int) -> List[str]:
        hours = [bin(n).count('1') for n in range(12)]
        mins = [bin(n).count('1') for n in range(60)]
        res = []
        for h, ho in enumerate(hours):
            for m, mo in enumerate(mins):
                if ho + mo == turnedOn:
                    res.append(str(h) + ":" + str(m).zfill(2))
        return res