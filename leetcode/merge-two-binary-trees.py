# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        def merger(node1, node2):
            if node1 and node2:
                new = TreeNode(node1.val + node2.val)
                new.left = merger(node1.left, node2.left)
                new.right = merger(node1.right, node2.right)
                return new
            if node2:
                new = TreeNode(node2.val)
                new.left = merger(node1, node2.left)
                new.right = merger(node1, node2.right)
                return new
                
            if node1:
                new = TreeNode(node1.val)
                new.left = merger(node1.left, node2)
                new.right = merger(node1.right, node2)
                return new
        return merger(root1, root2)



