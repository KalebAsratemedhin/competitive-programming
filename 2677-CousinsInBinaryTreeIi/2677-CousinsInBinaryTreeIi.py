# Last updated: 7/22/2025, 3:24:56 PM
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def replaceValueInTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        queue = deque([[root, root.val]])

        while queue:
            row_sum = 0

            for i in range(len(queue)):
                node, sibling = queue[i]
                row_sum += node.val


            for i in range(len(queue)):
                curr, sibling_sum = queue.popleft()
                curr.val = row_sum - sibling_sum
                child_sum = 0
                
                if curr.left:
                    child_sum += curr.left.val
                if curr.right:
                    child_sum += curr.right.val
                if curr.left:
                    queue.append([curr.left, child_sum])
                if curr.right:
                    queue.append([curr.right, child_sum])

        return root

                
            
