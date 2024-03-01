class Solution:
    def __init__(self):
        self.ans = 0
    def totalNQueens(self, n: int) -> int:
        col = [-1] * n
        diagonal = set()
        def helper(row):
            if row == n:
                self.ans += 1
            
            for j in range(n):
                if col[j] == -1 and row - j not in diagonal and row + j + n not in diagonal:
                    col[j] = row
                    diagonal.add(row - j)
                    diagonal.add(row + j + n)
                    helper(row + 1)
                    col[j] = -1
                    diagonal.remove(row - j)
                    diagonal.remove(row + j + n)

        helper(0)             

        return self.ans

