class Solution:
    def twoEditWords(self, queries: List[str], dictionary: List[str]) -> List[str]:
        def dist(w1, w2):
            if len(w1) == len(w2):
                strike = 0
                for c1, c2 in zip(w1, w2):
                    if c1 != c2:
                        strike += 1
                if strike <= 2:
                    return True
            return False
        res = []
        for q in queries:
            for w in dictionary:
                if dist(q, w):
                    res.append(q)
                    break
        return res