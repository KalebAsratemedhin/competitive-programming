# Last updated: 7/22/2025, 3:26:12 PM
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def spiralMatrix(self, m: int, n: int, head: Optional[ListNode]) -> List[List[int]]:
        direction = [(0, 1), (-1, 0), (0, -1), (1, 0)]

        matrix = [[-1 for i in range(n)] for j in range(m)]
        curr = head
        row, col = 0, -1

        def is_valid(r, c):
            return 0 <= r < m and 0 <= c < n and matrix[r][c] == -1

        while curr:
            for dx, dy in direction:
                while is_valid(row + dx, col + dy) and curr:
                    row, col = row + dx, col + dy
                    matrix[row][col] = curr.val
                    curr = curr.next

                
        return matrix



