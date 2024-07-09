# Problem: Binary Tree Right Side View - https://leetcode.com/problems/binary-tree-right-side-view/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        path = []
        queue = deque([root])
        while queue:
            r = len(queue)
            last = None
            for i in range(r):
                node = queue.popleft()
                if not node:
                    break
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                last = node
            if last:
                path.append(last.val)

        return path