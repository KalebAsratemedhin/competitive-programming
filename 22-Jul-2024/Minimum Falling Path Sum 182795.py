# Problem: Minimum Falling Path Sum - https://leetcode.com/problems/minimum-falling-path-sum/

class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        m, n = len(matrix), len(matrix[0])
        dp = [[0 for j in range(n)] for i in range(m)]
        dp[0] = matrix[0]

        for i in range(1, m):
            for j in range(n):

                if i < 1:
                    dp[i][j] = float("inf")
                    continue

                ans = float("inf")
                if j >= 1:
                    ans = min(ans, dp[i - 1][j - 1] + matrix[i][j])
                if j < n - 1:
                    ans = min(ans, dp[i - 1][j + 1] + matrix[i][j])
                
                dp[i][j] = min(ans, dp[i - 1][j] + matrix[i][j])
        
        return min(dp[m - 1])

              