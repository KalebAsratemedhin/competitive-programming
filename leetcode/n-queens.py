class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        col = [-1] * n
        ans = []
        diagonal = set()
        def helper(row):
            if row == n:
                ans.append(col.copy())
            
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
        res = []
        for a in ans:
            board = []
            for i in range(n):
                s = []
                for j in range(n):
                    if a[j] == i:
                        s.append("Q")
                    else:
                        s.append(".")
                board.append("".join(s))
            res.append(board)
                

        return res

