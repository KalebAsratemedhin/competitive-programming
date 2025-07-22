# Last updated: 7/22/2025, 3:27:14 PM
class Solution:
    def minOperations(self, grid: List[List[int]], x: int) -> int:

        arr = [grid[i][j] for i in range(len(grid)) for j in range(len(grid[0]))]
        arr.sort()
        
        median = len(arr) // 2
        steps = 0

        for num in arr:
            diff = abs(num - arr[median])
            if diff % x != 0:
                return -1
            steps += diff // x
        return steps