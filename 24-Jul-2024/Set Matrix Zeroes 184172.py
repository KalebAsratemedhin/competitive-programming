# Problem: Set Matrix Zeroes - https://leetcode.com/problems/set-matrix-zeroes/

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        empty = { 'row': set(), 'col': set()}
        
        m, n = len(matrix), len(matrix[0])
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    empty['row'].add(i)
                    empty['col'].add(j)

        for i in range(m):
            for j in range(n):
                if i in empty['row'] or j in empty['col']:
                    matrix[i][j] = 0


