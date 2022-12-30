class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        def dfs(node, path, res):
            if node == len(graph) - 1:
                res.append(path)
            for nei in graph[node]:
                dfs(nei, path + [nei], res)
        
        res = []
        dfs(0, [0], res)
        return res
