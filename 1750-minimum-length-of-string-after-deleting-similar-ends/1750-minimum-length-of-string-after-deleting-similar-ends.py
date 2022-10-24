sys.setrecursionlimit(10**6)
class Solution:
    def minimumLength(self, s: str) -> int:
        while s != "":
            if s[0] == s[-1] and len(s) > 1:
                i = 0
                j = len(s) - 1
                while i < len(s) - 1:
                    if s[i+1] == s[0]:
                        i += 1
                    else:
                        break
                while j > i:
                    if s[j-1] == s[0]:
                        j -= 1
                    else:
                        break
                if i == j:
                    return 0
                s = s[i+1:j]
                continue
            else:
                return len(s)