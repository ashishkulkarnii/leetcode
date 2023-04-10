class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for c in s:
            match c:
                case '(' | '[' | '{':
                    stack.append(c)
                case ')':
                    if not stack or stack.pop(-1) != '(':
                        return False
                case ']':
                    if not stack or stack.pop(-1) != '[':
                        return False
                case '}':
                    if not stack or stack.pop(-1) != '{':
                        return False
        return not stack