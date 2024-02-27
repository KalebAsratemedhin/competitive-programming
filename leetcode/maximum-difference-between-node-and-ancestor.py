# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.max_diff = 0
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        def helper(node, maxima, minima):
            if node:
                self.max_diff = max(self.max_diff, abs(maxima - node.val), abs(minima - node.val))
                helper(node.left, max(node.val, maxima), min(node.val, minima))
                helper(node.right, max(node.val, maxima), min(node.val, minima))
        helper(root, root.val, root.val)
        return self.max_diff