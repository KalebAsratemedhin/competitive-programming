# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.sum = 0
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        stack = []
        def helper(node):
            if not node:
                self.sum += int("".join(stack))
                return

            stack.append(str(node.val))
            if node.left and node.right:
                helper(node.left)
                helper(node.right)
            elif node.left:
                helper(node.left)
            else:
                helper(node.right)

            stack.pop()
        helper(root)
        return self.sum