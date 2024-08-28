# Problem: Count Sub Islands - https://leetcode.com/problems/count-sub-islands/

class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        
        def dfs(i, j): 
            if not (0 <= i < m and 0 <= j < n): 
                return 0
            if grid2[i][j] == -1:
                return -1
            if grid2[i][j] == 0: 
                return 0
            if grid2[i][j] == 1 and grid1[i][j] == 0: 
                grid2[i][j] = -1
                return -1

            grid2[i][j] = 0
            res = 1
            
            for dx, dy in [[-1, 0], [1, 0], [0, -1], [0, 1]]:
                compare = dfs(i + dx, j + dy)
                if compare < 0:
                    grid2[i][j] = -1
                    return -1
                res += compare
            return res
        
        m, n = len(grid1), len(grid1[0])
        ans = 0
        for i in range(m):
            for j in range(n):
                if grid2[i][j] == 1 and dfs(i, j) > 0:
                    ans += 1

        return ans