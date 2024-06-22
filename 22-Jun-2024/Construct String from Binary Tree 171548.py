# Problem: Construct String from Binary Tree - https://leetcode.com/problems/construct-string-from-binary-tree/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def tree2str(self, root: Optional[TreeNode]) -> str:
        def helper(node):
            if not node:
                return ''

            if not node.left and not node.right:
                return f"{node.val}"
            ans = f"{node.val}({helper(node.left)})"
            right = helper(node.right)
            
            if right:
                ans += f"({right})"
            return ans
            
        return helper(root)
            


