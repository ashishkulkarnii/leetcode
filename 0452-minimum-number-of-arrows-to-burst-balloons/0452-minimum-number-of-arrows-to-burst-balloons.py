class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort()
        stack = []
        for xi, xf in points:
            if stack and xi <= stack[-1][1]:
                stack[-1][1] = min(stack[-1][1], xf)
            else:
                stack.append([xi, xf])
        return len(stack)