class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        curr_max = -1
        for i in range(len(arr) - 1, -1, -1):
            curr = arr[i]
            arr[i] = curr_max
            curr_max = max(curr_max, curr)
        return arr