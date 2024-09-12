# Problem: Largest Local Values in a Matrix - https://leetcode.com/problems/largest-local-values-in-a-matrix/

class Solution:
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        n = len(grid)

        localMax = [[0 for i in range(n - 2)] for j in range(n - 2)]

        directions = [(0, 0), (0, 1), (1, 0), (1, 1), (-1, 0), (0, -1), (-1, -1), (1, -1), (-1, 1)]

        for i in range(n - 2):
            for j in range(n - 2):
                for dx, dy in directions:
                    
                    localMax[i][j] = max(localMax[i][j], grid[i + 1 + dx][j + 1 + dy])
        
        return localMax

