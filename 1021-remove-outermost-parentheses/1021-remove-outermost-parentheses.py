class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        stack = collections.deque()
        res = ""
        for i, c in enumerate(s):
            if c == "(":
                stack.append(i)
            else:
                if len(stack) > 1:
                    stack.pop()
                else:
                    res += s[stack.pop()+1:i]
        return res