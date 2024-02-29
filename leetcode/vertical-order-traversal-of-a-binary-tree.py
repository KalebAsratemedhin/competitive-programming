# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        ans = []
        def helper(node, col, row):
            if node:
                ans.append((col, row, node.val))
                helper(node.left, col - 1, row + 1)
                helper(node.right, col + 1, row + 1)
        helper(root, 0, 0)
        ans.sort()
        res = [[]]
        prev = ans[0][0]
        for a in ans:
            if a[0] == prev:
                res[-1].append(a[2])
            else:
                res.append([a[2]])
            prev = a[0]
        return res



