class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        m = len(matrix)
        n = len(matrix[0])
        for i in range(m):
            for j in range(n):
                r = i - 1
                c = j - 1
                if c >= 0 and r >= 0:
                    if matrix[i][j] != matrix[r][c]:
                        return False
        return True


