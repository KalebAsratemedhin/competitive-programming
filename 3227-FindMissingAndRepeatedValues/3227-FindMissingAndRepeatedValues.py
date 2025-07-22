# Last updated: 7/22/2025, 3:23:47 PM
class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        n = len(grid)
        dict = {}
        ans = [0, 0]
        for i in range(n):
            for j in range(n):
                if grid[i][j] in dict:
                    ans[0] = grid[i][j] 
                dict[grid[i][j]] = dict.get(grid[i][j], 0) + 1


        for i in range(1, n * n + 1):
            if i not in dict:
                ans[1] = i
        return ans