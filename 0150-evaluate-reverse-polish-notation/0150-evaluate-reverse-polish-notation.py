class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for operand in tokens:
            match operand:
                case '+':
                    stack.append(stack.pop(-1) + stack.pop(-1))
                case '-':
                    stack.append(-stack.pop(-1) + stack.pop(-1))
                case '*':
                    stack.append(stack.pop(-1) * stack.pop(-1))
                case '/':
                    stack.append(int(stack.pop(-2) / stack.pop(-1)))
                case _:
                    stack.append(int(operand))
        return stack[-1]