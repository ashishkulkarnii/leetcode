class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        stack = []
        for val in pushed:
            stack.append(val)
            while stack and popped and stack[-1] == popped[0]:
                stack.pop(-1)
                popped.pop(0)
        return not popped and not stack