class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        to_visit = set()
        visited = set()
        to_visit.add(0)
        while to_visit:
            curr = to_visit.pop()
            visited.add(curr)
            for room in rooms[curr]:
                if room not in visited:
                    to_visit.add(room)
        return len(visited) == len(rooms)