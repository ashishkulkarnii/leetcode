class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        to_visit = set()
        visited = set()
        to_visit.add(source)
        while to_visit:
            curr = to_visit.pop()
            visited.add(curr)
            for u, v in edges:
                if u == curr and v not in visited:
                    to_visit.add(v)
                elif v == curr and u not in visited:
                    to_visit.add(u)
            if destination in visited or destination in to_visit:
                return True
        return False