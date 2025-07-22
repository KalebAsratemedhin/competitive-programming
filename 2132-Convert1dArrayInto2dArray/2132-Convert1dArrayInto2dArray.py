# Last updated: 7/22/2025, 3:27:23 PM
class Solution:
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:

        if m * n < len(original) or m * n > len(original):
            return []

        ans = []
        for i in range(m):
            row = []
            for j in range(n):
                row.append(original[i * n + j])
            ans.append(row)
        return ans
