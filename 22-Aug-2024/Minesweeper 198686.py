# Problem: Minesweeper - https://leetcode.com/problems/minesweeper/

class Solution:
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        vectors = [(1, 0), (0, 1), (-1, 0), (0, -1), (1, 1), (-1, 1), (1, -1), (-1, -1)]
        m, n = len(board), len(board[0])
        seen = [[0 for j in range(n)] for i in range(m)]

        def inrange(row, col):
            return 0 <= row < m and 0 <= col < n

        def dfs(row, col):
            mines = 0
            seen[row][col] = 1
            for dx, dy in vectors:
                if inrange(row + dx, col + dy):
                    if board[row + dx][col + dy] == "M":
                        mines += 1

            if mines > 0:
                board[row][col] = str(mines)
                return 

            board[row][col] = "B"
            for dx, dy in vectors:
                if inrange(row + dx, col + dy):
                    if not seen[row + dx][col + dy] and board[row + dx][col + dy] == "E":
                        dfs(row + dx, col + dy)

        if board[click[0]][click[1]] == "M":
            board[click[0]][click[1]] = "X"
            return board

        dfs(click[0], click[1])
        return board