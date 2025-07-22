# Last updated: 7/22/2025, 3:23:03 PM
class Solution:
    def minTimeToReach(self, moveTime: List[List[int]]) -> int:
        m, n = len(moveTime), len(moveTime[0])
        ans = float("inf")
        directions = [(0, 1), (1, 0), (-1, 0), (0, -1)]
        visited = set()
        distances = [[float("inf") for j in range(n)] for i in range(m)]
        heap = [(0, 0, 0)]

        def is_valid(r, c):
            return 0 <= r < m and 0 <= c < n and (r, c) not in visited

        distances[0][0] = 0
        
        while heap:
            dist, r, c = heapq.heappop(heap)

            visited.add((r, c))

            for dx, dy in directions:
                r2, c2 = r + dx, c + dy

                if is_valid(r2, c2):
                    dist = max(distances[r][c], moveTime[r2][c2]) + 1
                    if dist < distances[r2][c2]:
                        distances[r2][c2] = dist
                        heapq.heappush(heap, (dist, r2, c2))
            

                    

        return distances[m - 1][n - 1]


