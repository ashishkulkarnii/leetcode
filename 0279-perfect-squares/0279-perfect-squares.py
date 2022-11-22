class Solution:
    def numSquares(self, n: int) -> int:
        visited = set()
        queue = [(0, 0)]
        while len(queue) > 0:
            x, f = queue.pop(0)
            squares = map(lambda x: x**2, count(1))
            for s in squares:
                nxt = s + x
                if nxt in visited:
                    continue
                elif nxt == n:
                    return f + 1
                elif nxt > n:
                    break
                visited.add(nxt)
                queue.append((nxt, f+1))