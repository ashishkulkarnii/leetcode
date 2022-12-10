class Solution:
    def gen(self, s, n, res):
        if n > 0:
            for i in range(len(s)+1):
                if i == 0 or s[i-1] == '(':
                    self.gen(s[:i]+'()'+s[i:], n-1, res)
        else:
            res.add(s)
    def generateParenthesis(self, n: int) -> List[str]:
        res = set()
        self.gen('', n, res)
        return list(res)