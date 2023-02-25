class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        def evaluate(string):
            stack = []
            for c in string:
                if c == '#':
                    if stack:
                        stack.pop(-1)
                else:
                    stack.append(c)
            return ''.join(stack)
        return evaluate(s) == evaluate(t)