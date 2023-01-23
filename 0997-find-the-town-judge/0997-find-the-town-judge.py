class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        trusted_by = dict()
        for i in range(1, n+1):
            trusted_by[i] = set()
        for truster, trustee in trust:
            if trustee in trusted_by.keys():
                trusted_by[trustee].add(truster)
        possible_judges = []
        trusters = set().union(*list(trusted_by.values()))
        for j in trusted_by.keys():
            if len(trusted_by[j]) == n - 1 and j not in trusters:
                possible_judges.append(j)
        return possible_judges[0] if len(possible_judges) == 1 else -1