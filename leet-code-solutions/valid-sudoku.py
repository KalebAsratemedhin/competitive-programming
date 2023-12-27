class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = {}
        cols = {}
        for i in range(9):
            if i % 3 == 0:
                temp = [{0}, {0},{0}]
            for j in range(9):
                if board[i][j] != '.':
                    if j in cols:
                        if board[i][j] in cols[j]:
                            return False
                        cols[j].add(board[i][j])
                    else:
                        cols[j] = {board[i][j]}
                    if i in rows:
                        if board[i][j] in rows[i]:
                            return False
                        rows[i].add(board[i][j])
                    else:
                        rows[i] = {board[i][j]}
                    if board[i][j] in temp[j // 3]:
                        return False
                    else: 
                        temp[j // 3].add(board[i][j])
        return True
            