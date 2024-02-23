# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def helper(node, p, q):
            if node.val == p.val or node.val == q.val:
                return node
            if p.val < node.val and q.val > node.val:
                return node
            if p.val > node.val and q.val < node.val:
                return node
            if p.val < node.val and q.val < node.val:
                return helper(node.left, p, q)
            if p.val > node.val and q.val > node.val:
                return helper(node.right, p, q)
        return helper(root, p, q)
            
            
            
            