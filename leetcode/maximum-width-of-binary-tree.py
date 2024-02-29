# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        deq = deque()
        deq.append([1, root])
        maxima = 0

        while deq:
            maxima = max(maxima, deq[-1][0] - deq[0][0] + 1)
            for i in range(len(deq)):
                pair = deq.popleft()
                if pair[1].left:
                    deq.append([pair[0] * 2, pair[1].left])
                if pair[1].right:
                    deq.append([pair[0] * 2 + 1, pair[1].right])
        return maxima
        