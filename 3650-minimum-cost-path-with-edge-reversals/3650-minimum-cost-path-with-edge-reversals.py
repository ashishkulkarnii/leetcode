class Solution:
    def minCost(self, n: int, edges: List[List[int]]) -> int:
        edge_cost = dict()
        e = collections.defaultdict(set)
        for s, d, cost in edges:
            edge_cost[(s, d)] = min(cost, edge_cost.get((s, d), float('inf')))
            edge_cost[(d, s)] = min(cost * 2, edge_cost.get((d, s), float('inf')))
            e[s].add(d)
            e[d].add(s)
        dist = [float('inf') for _ in range(n)]
        dist[0] = 0
        pq = [(0, 0)]
        while pq:
            cost, curr = heapq.heappop(pq)
            for node in list(e[curr]):
                tmp_cost = cost + edge_cost.get((curr, node))
                if tmp_cost < dist[node]:
                    dist[node] = tmp_cost
                    heapq.heappush(pq, (tmp_cost, node))
        return dist[-1] if dist[-1] < float('inf') else -1
