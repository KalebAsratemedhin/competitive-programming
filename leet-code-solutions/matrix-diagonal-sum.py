class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        total = 0
        n = len(mat)
        for i in range(n):
            for j in range(n):
                if i - j == 0:
                    total += mat[i][j]
                elif i + j == n - 1:
                    total += mat[i][j]
        return total