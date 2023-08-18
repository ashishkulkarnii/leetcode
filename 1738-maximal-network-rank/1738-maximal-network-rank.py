class Solution:
    def maximalNetworkRank(self, n: int, roads: List[List[int]]) -> int:
        max_network_rank = 0
        city_roads = collections.defaultdict(int)
        city_connection = set()
        for c1, c2 in roads:
            city_roads[c1] += 1
            city_roads[c2] += 1
            city_connection.add(tuple([min((c1, c2)), max((c1, c2))]))
        city_roads = list(city_roads.items())
        for i, (c1, r1) in enumerate(city_roads[:-1]):
            for j, (c2, r2) in enumerate(city_roads[i+1:]):
                network_rank = r1 + r2 - (1 if tuple([min((c1, c2)), max((c1, c2))]) in city_connection else 0)
                max_network_rank = max(max_network_rank, network_rank)
        return max_network_rank