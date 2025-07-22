# Last updated: 7/22/2025, 3:25:00 PM
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthLargestLevelSum(self, root: Optional[TreeNode], k: int) -> int:
        level_sums = []
        queue = deque([root])
        

        while queue:
            curr_sum = 0
            

            for i in range(len(queue)):
                node = queue.popleft()
                curr_sum += node.val
                if node.left:
                    queue.append(node.left)
                    
                if node.right:
                    queue.append(node.right)

            level_sums.append(curr_sum)
        
        if k > len(level_sums):
            return -1

        level_sums.sort()
        return level_sums[-k ]

