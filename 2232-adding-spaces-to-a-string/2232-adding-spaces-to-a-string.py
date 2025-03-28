class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        i = 0
        j = 0
        n = 0
        res = ""
        while i < len(s) and j < len(spaces):
            if n == spaces[j]:
                res += " "
                j += 1
            else:
                res += s[i]
                i += 1
                n += 1
        return res + s[i:]