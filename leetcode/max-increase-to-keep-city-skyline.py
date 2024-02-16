class Solution:
    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
        n = len(grid)
        row_max = [0] * n
        col_max = [0] * n
        ans = 0

        for i in range(n):
            for j in range(n):
                row_max[i] = max(row_max[i], grid[i][j])
                col_max[j] = max(col_max[j], grid[i][j])
        
        for i in range(n):
            for j in range(n):
                updated = min(row_max[i], col_max[j])
                ans += updated - grid[i][j] 
                grid[i][j] = updated
        
        return ans
        