# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.max_sum = 0
    def maxSumBST(self, root: Optional[TreeNode]) -> int:
        def helper(node):
            if not node:
                return [True, float('inf'), float('-inf'), 0]
            if node:
                [left_valid, left_min, left_max, left_total] = helper(node.left)
                [right_valid, right_min, right_max, right_total] = helper(node.right)

                if left_valid and right_valid and left_max < node.val < right_min:
                    subtree = left_total + right_total + node.val
                    self.max_sum = max(self.max_sum, subtree)
                    
                    return [True, min(left_min, node.val), max(right_max, node.val), subtree]
                return [False, 0,0,0]
        helper(root)
        return self.max_sum
        