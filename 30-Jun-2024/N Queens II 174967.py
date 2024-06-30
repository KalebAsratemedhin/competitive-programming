# Problem: N Queens II - https://leetcode.com/problems/n-queens-ii/

class Solution:
    def __init__(self):
        self.ans = 0
    def totalNQueens(self, n: int) -> int:
        board_1d = [-1] * n
        diagonal = set()
        def helper(row):
            if row == n:
                self.ans += 1
            
            for col in range(n):
                if board_1d[col] == -1 and row - col not in diagonal and row + col + n not in diagonal:
                    board_1d[col] = row
                    diagonal.add(row - col)
                    diagonal.add(row + col + n)
                    helper(row + 1)
                    board_1d[col] = -1
                    diagonal.remove(row - col)
                    diagonal.remove(row + col + n)

        helper(0)             

        return self.ans
