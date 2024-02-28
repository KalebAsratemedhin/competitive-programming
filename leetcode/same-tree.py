# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        def isSame(p, q):
            if p and q:
                if p.val == q.val:
                    left = isSame(p.left, q.left)
                    right = isSame(p.right, q.right)
                    return left and right
                return False
            if not p and not q:
                return True
            if not p or not q:
                return False
            
        return isSame(p, q)