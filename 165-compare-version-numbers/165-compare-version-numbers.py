class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        v1 = list(map(int, version1.split('.')))
        v2 = list(map(int, version2.split('.')))
        l1 = len(v1)
        l2 = len(v2)
        r = 1
        if l1 < l2:
            l1, l2 = l2, l1
            v1, v2 = v2, v1
            r = -1
        v2.extend([0]*(l1-l2))
        for i in range(l1):
            if v1[i] > v2[i]:
                return r
            if v1[i] < v2[i]:
                return -r
        return 0