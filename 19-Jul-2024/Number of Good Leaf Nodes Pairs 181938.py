# Problem: Number of Good Leaf Nodes Pairs - https://leetcode.com/problems/number-of-good-leaf-nodes-pairs/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.goods = 0
    def countPairs(self, root: TreeNode, distance: int) -> int:
        
        def dfs(node):
            if not node:
                return []
            
            left = dfs(node.left)
            right = dfs(node.right)

            for i in range(len(right)):
                right[i] += 1

            for i in range(len(left)):
                left[i] += 1 

            for i in left:
                for j in right:
                    if i + j <= distance:
                        self.goods += 1

            combo = right + left
            if not len(combo):
                return [0]
            return combo

        dfs(root)
        return self.goods