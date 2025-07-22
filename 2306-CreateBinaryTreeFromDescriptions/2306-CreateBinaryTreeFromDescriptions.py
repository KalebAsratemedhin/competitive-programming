# Last updated: 7/22/2025, 3:26:31 PM
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def createBinaryTree(self, descriptions: List[List[int]]) -> Optional[TreeNode]:
        n = len(descriptions) + 1
        indegrees = {}
        children = defaultdict(lambda: [-1, -1])
        parents = set()


        for parent, child, is_left in descriptions:
            if is_left:
                children[parent][0] = child
            else:
                children[parent][1] = child
            indegrees[child] = 1
            parents.add(parent)

        root = -1
        for parent in parents:
            if parent not in indegrees:
                root = parent

        def recurse(val, left, right):
            node = TreeNode(val)
            if left != -1:
                a, b = children[left]
                node.left = recurse(left, a, b)
            if right != -1:
                a, b = children[right]
                node.right = recurse(right, a, b)
            return node


        a, b = children[root]
        return recurse(root, a, b)
            


