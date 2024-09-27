# Problem: N-ary Tree Postorder Traversal - https://leetcode.com/problems/n-ary-tree-postorder-traversal/

"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        path = []

        def post_helper(node):
            if node:
                for child in node.children:
                    post_helper(child)
                path.append(node.val)

        post_helper(root)
        return path
                