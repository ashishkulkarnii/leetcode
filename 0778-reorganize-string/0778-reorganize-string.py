class Solution:
    def reorganizeString(self, s: str) -> str:
        s = list(s)
        c = sorted([[char, freq] for char, freq in collections.Counter(s).items()], key=lambda x: x[1], reverse=True)
        res = c[0][0]
        c[0][1] -= 1
        if c[0][1] <= 0:
            c.pop(0)
        while len(res) < len(s):
            c = sorted(c, key=lambda x: x[1], reverse=True)
            ptr = 0
            while c[ptr][0] == res[-1]:
                ptr += 1
                if ptr == len(c):
                    return ""
            res += c[ptr][0]
            c[ptr][1] -= 1
            if c[ptr][1] <= 0:
                c.pop(ptr)
        return res