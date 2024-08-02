# Problem: Kth Smallest Element in a BST - https://leetcode.com/problems/kth-smallest-element-in-a-bst/

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
        def dfs(node):
            if node:
                left = dfs(node.left)
                if left != None:
                    return left
                self.count += 1

                if self.count == k:
                    return node.val
                return dfs(node.right)


        return dfs(root)
