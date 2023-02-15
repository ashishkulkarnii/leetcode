class Solution:
    def areNumbersAscending(self, s: str) -> bool:
        arr = [int(n) for n in s.split() if n.isnumeric()]
        return arr == sorted(arr) and len(arr) == len(set(arr))