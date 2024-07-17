# Problem: Delete Nodes And Return Forest - https://leetcode.com/problems/delete-nodes-and-return-forest/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def delNodes(self, root: Optional[TreeNode], to_delete: List[int]) -> List[TreeNode]:
        to_delete = set(to_delete)
        components = []
        
        def dfs(node):
            if node:
                left = dfs(node.left)
                right = dfs(node.right)
                node.left = left
                node.right = right

                if node.val in to_delete:
                    if node.left: components.append(node.left)
                    if node.right: components.append(node.right)
                    node.left = None
                    node.right = None
                    return None
                return node

        dfs(root)
        if root and root.val not in to_delete: components.insert(0, root)
        return components
