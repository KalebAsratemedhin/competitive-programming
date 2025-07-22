# Last updated: 7/22/2025, 3:25:38 PM
class Solution:
    def maxSum(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        maximal = 0
        for i in range(m - 2):
            for j in range(n - 2):
                sum = 0
                for k in range(3):
                    sum += grid[i][j + k]
                    sum += grid[i + 2][j + k]
                sum += grid[i + 1][j + 1]
                maximal = max(sum, maximal)
        return maximal
            


