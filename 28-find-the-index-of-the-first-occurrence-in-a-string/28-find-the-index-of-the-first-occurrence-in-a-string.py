class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        for i in range(len(haystack) - len(needle) + 1):
            for j in range(len(needle)):
                x = i
                y = 0
                while(x-i<=len(needle)-1):
                    if haystack[x] == needle[y]:
                        x+=1
                        y+=1
                    else:
                        break
                if x-i == len(needle):
                    return i
        return -1
            