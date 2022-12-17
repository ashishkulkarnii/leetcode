class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        i = 0
        while i < len(tokens):
            operand = tokens[i]
            if operand == '+':
                tokens[i-2] = int(tokens[i-2]) + int(tokens[i-1])
                tokens.pop(i)
                tokens.pop(i-1)
                i -= 1
            elif operand == '-':
                tokens[i-2] = int(tokens[i-2]) - int(tokens[i-1])
                tokens.pop(i)
                tokens.pop(i-1)
                i -= 1
            elif operand == '*':
                tokens[i-2] = int(tokens[i-2]) * int(tokens[i-1])
                tokens.pop(i)
                tokens.pop(i-1)
                i -= 1
            elif operand == '/':
                tokens[i-2] = int(int(tokens[i-2]) / int(tokens[i-1]))
                tokens.pop(i)
                tokens.pop(i-1)
                i -= 1
            else:
                i += 1
        return int(tokens[-1])