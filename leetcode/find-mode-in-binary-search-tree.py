# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        modes = {}
        def helper(node, maxima):
            if node:
                modes[node.val] = modes.get(node.val, 0) + 1
                maxima = max(maxima, modes[node.val])
                maxima = max(maxima, helper(node.left, maxima))
                maxima = max(maxima, helper(node.right, maxima))

            return maxima
        maxima = helper(root, 0)
        ans = []
        for key, value in modes.items():
            if value == maxima:
                ans.append(key)
        return ans