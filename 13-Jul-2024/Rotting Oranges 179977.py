# Problem: Rotting Oranges - https://leetcode.com/problems/rotting-oranges/

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        queue = deque()
        m, n = len(grid), len(grid[0])
        freshes = 0
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2:
                    queue.append((i, j))
                if grid[i][j] == 1:
                    freshes += 1

        directions = [(0, 1), (1, 0), (-1, 0), (0, -1)]

        def is_valid(row, col):
            return 0 <= row < m and 0 <= col < n and grid[row][col] == 1
        
        def dfs(freshes):
            
            minutes = 0
            while queue and freshes:
                for i in range(len(queue)):
                    row, col = queue.popleft()

                    for dx, dy in directions:
                        if is_valid(row + dx, col + dy):
                            grid[row + dx][col + dy] = 2
                            queue.append((row + dx, col + dy))
                            freshes -= 1


                minutes += 1
            if freshes: return -1
            return minutes

        return dfs(freshes)

        

