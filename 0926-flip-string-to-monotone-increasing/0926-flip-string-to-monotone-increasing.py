class Solution:
    def minFlipsMonoIncr(self, s: str) -> int:
        ones = 0
        ans = 0
        for c in s:
            match(c):
                case '0':
                    ans = min(ones, ans + 1)
                case '1':
                    ones += 1
        return ans