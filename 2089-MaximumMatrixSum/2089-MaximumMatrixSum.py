# Last updated: 7/22/2025, 3:27:35 PM
class Solution:
    def maxMatrixSum(self, matrix: List[List[int]]) -> int:
        smallest_pos = float('inf')
        biggest_neg = float('-inf')
        total = 0
        negative_nums = 0
        found_zero = False

        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                num = matrix[i][j]
                if num > 0:
                    smallest_pos = min(num, smallest_pos) 
                    total += num
                elif num == 0:
                    found_zero = True
                else:
                    biggest_neg = max(biggest_neg, num)
                    negative_nums += 1
                    total += abs(num)
   

        if biggest_neg == float('-inf') or found_zero or negative_nums % 2 == 0:
            return total

        return total + 2 * max(biggest_neg, smallest_pos * -1)


