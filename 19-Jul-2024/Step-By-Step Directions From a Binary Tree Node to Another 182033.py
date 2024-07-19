# Problem: Step-By-Step Directions From a Binary Tree Node to Another - https://leetcode.com/problems/step-by-step-directions-from-a-binary-tree-node-to-another/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getDirections(self, root: Optional[TreeNode], startValue: int, destValue: int) -> str:
        start_path, dest_path = [], []
        def dfs(node, target, path):
            if node:
                if node.val == target:
                    return True
                
                if dfs(node.left, target, path):
                    path.append('L')
                    return True
                
                if dfs(node.right, target, path):
                    path.append('R')
                    return True

        dfs(root, startValue, start_path)
        dfs(root, destValue, dest_path)

        start_path = "".join(start_path[::-1])
        dest_path = "".join(dest_path[::-1])

        common = min(len(start_path), len(dest_path))
        for i in range(common):
            if start_path[i] != dest_path[i]:
                return "U" * (len(start_path) - i) + dest_path[i:]
            
        return "U" * (len(start_path) - common) + dest_path[common:]