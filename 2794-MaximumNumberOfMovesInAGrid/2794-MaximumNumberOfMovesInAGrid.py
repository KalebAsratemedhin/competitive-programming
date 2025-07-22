# Last updated: 7/22/2025, 3:24:31 PM
class Solution:
    def maxMoves(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        dp = [[0 if i == 0 else -1 for i in range(n)] for j in range(m)]

        for i in range(1, n):
            for j in range(m):
                if j - 1 >= 0 and dp[j - 1][i - 1] != -1 and grid[j - 1][i - 1] < grid[j][i]:
                    dp[j][i] = max(dp[j - 1][i - 1] + 1, dp[j][i])

                if dp[j][i - 1] != -1 and grid[j][i - 1] < grid[j][i]:
                    dp[j][i] = max(dp[j][i - 1] + 1, dp[j][i])

                if j + 1 < m and dp[j + 1][i - 1] != -1 and grid[j + 1][i - 1] < grid[j][i]:
                    dp[j][i] = max(dp[j + 1][i - 1] + 1, dp[j][i])



        max_moves = 0
        for i in range(m):
            for j in range(n):
                max_moves = max(dp[i][j], max_moves)
        return max_moves
