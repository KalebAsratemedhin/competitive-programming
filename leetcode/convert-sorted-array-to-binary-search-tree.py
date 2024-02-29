# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        
        def helper(left, right):
            if right < left:
                return None

            mid = (left + right) // 2
            left_branch = helper(left, mid - 1)
            right_branch = helper(mid + 1, right)
            return TreeNode(nums[mid], left_branch, right_branch)
        return helper(0, len(nums) - 1)


