# Problem: Sudoku Solver - https://leetcode.com/problems/sudoku-solver/description/

class Solution:
    def __init__(self):
        self.ans = 0
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        given_row = {}
        given_col = {}
        sub_grids = defaultdict(lambda: set())
        spaces = []

        for i in range(9):
            st = set()
            for j in range(9):

                if board[i][j] != ".":
                    st.add(int(board[i][j]))
                    if (i // 3, j // 3) in sub_grids:
                        sub_grids[(i // 3, j // 3)].add(int(board[i][j]))
                    else:
                        sub_grids[(i // 3, j // 3)] = {int(board[i][j])}

                    if j in given_col:
                        given_col[j].add(int(board[i][j]))
                    else:
                        given_col[j] = {int(board[i][j])}
                else:
                    spaces.append([i,j,0])

            given_row[i] = st

        def helper(start):
            if start >= len(spaces):
                self.ans = copy.deepcopy(spaces)
                return
            
            for j in range(1,10):
                if j not in given_row[spaces[start][0]] and j not in given_col[spaces[start][1]] and j not in sub_grids[(spaces[start][0] // 3, spaces[start][1] //3)]:
                    
                    given_row[spaces[start][0]].add(j)
                    given_col[spaces[start][1]].add(j)
                    sub_grids[(spaces[start][0] // 3, spaces[start][1] //3)].add(j)
                    spaces[start][2] = j
                    helper(start + 1)
                    spaces[start][2] = 0
                    given_row[spaces[start][0]].remove(j)
                    given_col[spaces[start][1]].remove(j)
                    sub_grids[(spaces[start][0] // 3, spaces[start][1] //3)].remove(j)
                
        helper(0)
        ind = 0
        for i in range(9):
            for j in range(9):
                if board[i][j] == ".":
                    board[i][j] = str(self.ans[ind][2])
                    ind += 1
            