class Solution:
    def gen(self, s, n, res):
        if n > 0:
            for i in range(len(s)+1):
                self.gen(s[:i]+'()'+s[i:], n-2, res)
        else:
            res.append(s)
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        self.gen('', n*2, res)
        return list(set(res))