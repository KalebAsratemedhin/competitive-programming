# Last updated: 7/22/2025, 3:26:24 PM
class Solution:
    def countUnguarded(self, m: int, n: int, guards: List[List[int]], walls: List[List[int]]) -> int:
        # init grid with 0s
        # mark guards with 1s and walls with -1s
        # for every guard do a dfs and mark its neightbors 1 until you can't move further
        # count 0s

        grid = [[0 for j in range(n)] for i in range(m)]
        directions = [(0, 1), (1, 0), (-1, 0), (0, -1)]

        def is_valid(r, c):
            return 0 <= r < m and 0 <= c < n and grid[r][c] not in {-1, 1}

        for x, y in guards:
            grid[x][y] = 1

        for x, y in walls:
            grid[x][y] = -1

        for x, y in guards:
            for dx, dy in directions:
                r, c = x + dx, y + dy

                while is_valid(r, c):
                    grid[r][c] = 2
                    r, c = r + dx, c + dy


        counts = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:
                    counts += 1
        return counts



        
        

        
