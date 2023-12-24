class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        for i in range(n):
            for j in range(i,n):
                matrix[i][j],matrix[j][i] = matrix[j][i],matrix[i][j]

        for row in matrix:
            l,r = 0, n-1
            while l <= r:
                    row[r],row[l] = row[l], row[r]
                    l += 1
                    r -= 1
        