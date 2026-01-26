class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        arr.sort()
        m = abs(arr[1] - arr[0])
        for i, n in enumerate(arr[:-1]):
            m = min(m, abs(n - arr[i+1]))
        pairs = []
        for i, n in enumerate(arr[:-1]):
            if abs(n - arr[i+1]) == m:
                pairs.append(sorted([n, arr[i+1]]))
        return pairs