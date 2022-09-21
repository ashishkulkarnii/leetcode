class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        temp = ""
        for i in range(len(s)):
            if s[i] != ']':
                stack.append(s[i])
            else:
                while stack[-1] != '[':
                    temp = temp + stack[-1]
                    stack.pop(-1)
                stack.pop(-1)
                x = 1
                n = 0
                while len(stack):
                    if stack[-1].isdigit():
                        n += int(stack.pop(-1)) * x
                        x *= 10
                    else: break
                temp = temp[::-1] * n
                for c in temp:
                    stack.append(c)
                temp = ""
        return ''.join(stack)