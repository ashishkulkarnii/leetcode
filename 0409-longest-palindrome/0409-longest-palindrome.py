class Solution:
    def longestPalindrome(self, s: str) -> int:
        res = 0
        letters = set(list(s))
        odd = False
        for i in list(letters):
            if s.count(i) % 2 == 0:
                res += s.count(i)
            else:
                res += s.count(i) - 1
                odd = True
        return res + odd