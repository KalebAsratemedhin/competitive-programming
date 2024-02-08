class Solution:
    def numSubmatrixSumTarget(self, matrix: List[List[int]], target: int) -> int:
        n = len(matrix[0])
        m = len(matrix)
        count = 0

        for i in range(m):
            for j in range(1, n):
                matrix[i][j] += matrix[i][j - 1]

        for i in range(n):
            for j in range(i, n):
                prefix = {0: 1}
                total = 0
                for k in range(m):
                    if i > 0:
                        total -= matrix[k][i - 1]
                    total += matrix[k][j]
                    count += prefix.get(total - target, 0)
                    prefix[total] = prefix.get(total, 0) + 1
        return count


