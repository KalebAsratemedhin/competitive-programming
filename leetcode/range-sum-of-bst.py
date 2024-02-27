# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.sum = 0
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        def helper(node):
            if node:
                if node.val <= high and node.val >= low:
                    self.sum += node.val
                helper(node.left)
                helper(node.right)
        helper(root)
        return self.sum