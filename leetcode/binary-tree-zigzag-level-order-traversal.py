# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        ans = {}

        def zigzag(node, level = 0):
            if not node:
                return
            if level in ans:
                ans[level].append(node.val)
            else:
                ans[level] = [node.val]
            
            if node.left:
                left = zigzag(node.left, level + 1)
            if node.right:
                right = zigzag(node.right, level + 1)
            return
           

        zigzag(root)
        arr = []
        i = 0
        while i in ans:
            if i % 2 == 0:
                arr.append(ans[i])
            else:
                arr.append(ans[i][::-1])
            i += 1

        return arr
