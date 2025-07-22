# Last updated: 7/22/2025, 3:23:02 PM
class Solution:
    def minTimeToReach(self, moveTime: List[List[int]]) -> int:
        m, n = len(moveTime), len(moveTime[0])
        visited = set()
        distances = [[float("inf") for j in range(n)] for i in range(m)]
        directions = [(0, 1), (1, 0), (-1, 0), (0, -1)]

        distances[0][0] = 0

        heap = [(0, 0, 0, 1)]

        def is_valid(r, c):
            return  0 <= r < m and 0 <= c < n and (r, c) not in visited
        
        while heap:
            dist, r, c, cost = heapq.heappop(heap)

            visited.add((r, c))

            for dx, dy in directions:
                r2, c2 = r + dx, c + dy

                if is_valid(r2, c2):
                    new_dist = max(dist, moveTime[r2][c2]) + cost

                    if new_dist < distances[r2][c2]:
                        distances[r2][c2] = new_dist
                        heapq.heappush(heap, (new_dist, r2, c2, 3 - cost))
        
        return distances[m - 1][n - 1]

                    