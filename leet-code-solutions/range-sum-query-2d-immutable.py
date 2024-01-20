class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.prefix = matrix
        self.sumPrefix()
    def sumPrefix(self):
        n = len(self.prefix)
        m = len(self.prefix[0])
        for i in range(n):
            for j in range(m):
                if i >= 1 and j >= 1:
                    self.prefix[i][j] -= self.prefix[i - 1][j - 1]
                if i >= 1:
                    self.prefix[i][j] += self.prefix[i - 1][j]
                if j >= 1:
                    self.prefix[i][j] += self.prefix[i][j - 1]
                
    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        ans = self.prefix[row2][col2]
        if row1 >= 1:
            ans -= self.prefix[row1 - 1][col2]
        if col1 >= 1:
            ans -= self.prefix[row2][col1 -1]
        if row1 >= 1 and col1 >= 1:
            ans += self.prefix[row1 - 1][col1 - 1]
        return ans

        


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)