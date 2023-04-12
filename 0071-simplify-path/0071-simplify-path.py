class Solution:
    def simplifyPath(self, path: str) -> str:
        dirs = path.split('/')
        stack = list()
        for dir in dirs:
            if len(dir) == 0 or dir == '.':
                pass
            elif dir == '..':
                if stack:
                    stack.pop(-1)
            else:
                stack.append(dir)
        path = '/' + '/'.join(stack)
        return path