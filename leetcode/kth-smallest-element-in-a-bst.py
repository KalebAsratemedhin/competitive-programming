# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.count = 0
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        def helper(node):
            if node:
                left = helper(node.left)
                if left != None:
                    return left
                self.count += 1
                if self.count == k:
                    return node.val
                return helper(node.right)


        return helper(root)
