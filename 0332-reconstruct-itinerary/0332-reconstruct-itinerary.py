class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        graph = defaultdict(list)
        for src, dest in sorted(tickets, reverse=True):
            graph[src].append(dest)
        itinerary = []
        def dfs(node):
            while graph[node]:
                dfs(graph[node].pop())
            itinerary.append(node)
        dfs("JFK")
        return itinerary[::-1]