# Problem: Map of Highest Peak - https://leetcode.com/problems/map-of-highest-peak/description/

class Solution:
    def highestPeak(self, isWater: List[List[int]]) -> List[List[int]]:
        arr = deque()
        m, n = len(isWater), len(isWater[0])
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        for i in range(m):
            for j in range(n):
                if isWater[i][j] == 1:
                    arr.append((0, i, j))
                    
        ans = [[-1] * n for i in range(m)]
        while arr:
            val, x, y = arr.popleft() 
            if ans[x][y] != -1: 
                continue
            ans[x][y] = val
            for dx, dy in directions:
                if 0 <= x + dx < m and 0 <= y + dy < n and ans[x + dx][y + dy] == -1:
                    arr.append((val+1, x + dx, y + dy))
        return ans