class Solution:
    def distinctNames(self, ideas: List[str]) -> int:
        sets = [set() for _ in range(26)]
        for idea in ideas:
            sets[ord(idea[0]) - ord('a')].add(idea[1::])
        res = 0
        for i in range(25):
            for j in range(i + 1, 26):
                duplicates = len(sets[i].intersection(sets[j]))
                res += (len(sets[i]) - duplicates) * (len(sets[j]) - duplicates) * 2
        return res