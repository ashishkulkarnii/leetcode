class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        n = len(senate)
        Rs = [i for i, senator in enumerate(senate) if senator == 'R']
        Ds = [i for i, senator in enumerate(senate) if senator == 'D']
        while Rs and Ds:
            r = Rs.pop(0)
            d = Ds.pop(0)
            if r < d:
                Rs.append(r + n)
            else:
                Ds.append(d + n)
        return 'Radiant' if Rs else 'Dire'
                