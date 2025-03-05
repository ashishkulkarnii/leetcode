class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        res = set()
        for w1 in words:
            for w2 in words:
                if w2 in w1 and w1 != w2:
                    res.add(w2)
        return list(res)