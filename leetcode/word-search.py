class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m = len(board)
        n = len(board[0])
        def helper(start, x, y):
            if start == len(word) - 1:
                if board[x][y] == word[start]:
                    return True
                return False
            
            if board[x][y] != word[start]:
                return False

            temp = board[x][y]
            board[x][y] = "-1"

            if 0 <= x + 1 < m and 0 <= y < n and board[x + 1][y] != "-1":
                if helper(start + 1, x + 1, y):
                    return True
            if 0 <= x < m and 0 <= y + 1 < n and board[x][y + 1] != "-1":
                if helper(start + 1, x, y + 1):
                    return True
            if 0 <= x - 1 < m and 0 <= y < n and board[x - 1][y] != "-1":
                if helper(start + 1, x - 1, y):
                    return True
            if 0 <= x < m and 0 <= y - 1 < n and board[x][y - 1] != "-1":
                if helper(start + 1, x, y - 1):
                    return True
            board[x][y] = temp
            return False

        for i in range(m):
            for j in range(n):
                if board[i][j] == word[0] and helper(0, i, j):
                    return True
        return False

