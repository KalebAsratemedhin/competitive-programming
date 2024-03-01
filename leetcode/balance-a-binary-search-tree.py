# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:
        ans = []
        def inorder(node):
            if node:
                inorder(node.left)
                ans.append(node.val)
                inorder(node.right)
        inorder(root)
        print(ans)

        def divider(arr):
            if not arr:
                return None
            
            mid = len(arr) // 2
            left = divider(arr[:mid])
            right = divider(arr[mid + 1:])
            return TreeNode(arr[mid], left, right)
        return divider(ans)
        
        