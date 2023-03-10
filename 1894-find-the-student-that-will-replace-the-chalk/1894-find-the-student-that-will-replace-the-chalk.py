class Solution:
    def chalkReplacer(self, chalk: List[int], k: int) -> int:
        k = k % sum(chalk)
        for i, c in enumerate(chalk):
            if c > k:
                return i
            k -= c
        return 0