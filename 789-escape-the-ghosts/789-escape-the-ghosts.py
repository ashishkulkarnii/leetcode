class Solution:
    def escapeGhosts(self, ghosts: List[List[int]], target: List[int]) -> bool:
        closest_ghost = abs(ghosts[0][0] - target[0]) + abs(ghosts[0][1] - target[1])
        for ghost in ghosts:
            closest_ghost = min(closest_ghost, abs(ghost[0] - target[0]) + abs(ghost[1] - target[1]))
        return closest_ghost > abs(target[0]) + abs(target[1])