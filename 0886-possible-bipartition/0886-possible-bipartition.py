class Solution:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        if not dislikes:
            return True
        adj_list = [[] for i in range(n)]
        for a, b in dislikes:
            adj_list[a-1].append(b-1) 
            adj_list[b-1].append(a-1)
        vertices = sorted(list(range(n)), key=lambda x: len(adj_list[x]))[::-1]
        colors = [0] * n
        colors[vertices[0]] = 1
        for v in vertices:
            if colors[v] != 0:
                neighbors = adj_list[v]
                for n in neighbors:
                    if colors[n] == colors[v]:
                        return False
                    colors[n] = -colors[v]
        return True