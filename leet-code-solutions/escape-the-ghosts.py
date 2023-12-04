class Solution:
    def escapeGhosts(self, ghosts: List[List[int]], target: List[int]) -> bool:
        distance = abs(target[0]) + abs(target[1])
        for g in range(len(ghosts)):
            ghost_distance = abs(ghosts[g][0] - target[0]) + abs(ghosts[g][1] - target[1])
            if ghost_distance <= distance:
                return False
        return True