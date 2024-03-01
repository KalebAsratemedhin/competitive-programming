# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
        def helper(arr):
            if not arr:
                return None
            maxima = max(arr)
            idx = arr.index(maxima)

            left = helper(arr[:idx])
            right = helper(arr[idx + 1:])
            return TreeNode(maxima, left, right)
        return helper(nums)