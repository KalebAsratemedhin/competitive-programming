class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        m = len(mat)
        n = len(mat[0])
        s = m + n - 1
        ans = []
        for k in range(s):
            if k < n:
                j = k
                i = 0
            elif k >= n:
                i = k - n + 1
                j = n - 1
            temp = []
            while  i < m and j >= 0:
                temp.append(mat[i][j])
                i += 1
                j -= 1
            if k % 2 == 0:
                ans += temp[::-1]
            else:
                ans += temp
        return ans

                

