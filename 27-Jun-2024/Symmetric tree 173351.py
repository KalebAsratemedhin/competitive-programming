# Problem: Symmetric tree - https://leetcode.com/problems/symmetric-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def helper(node1, node2):
            if not node1 and not node2:
                return True

            if node1 and node2:
                if node1.val == node2.val:
                    left = helper(node1.right, node2.left)
                    right = helper(node1.left, node2.right)
                    return left and right
            return False
        return helper(root.left, root.right)