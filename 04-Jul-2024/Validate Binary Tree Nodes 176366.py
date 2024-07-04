# Problem: Validate Binary Tree Nodes - https://leetcode.com/problems/validate-binary-tree-nodes/

class Solution:
    def validateBinaryTreeNodes(self, n: int, leftChild: List[int], rightChild: List[int]) -> bool:
        colors = [0 for i in range(n)]
        indegree_zeros = {i for i in range(n)} - (set(leftChild) | set(rightChild))      

        def dfs(node):
            if node != -1:
                if colors[node] == 2 or colors[node] == 1:
                    return False
                else:
                    colors[node] = 1
                    if not dfs(leftChild[node]) or not dfs(rightChild[node]):
                        return False
                    colors[node] = 2
                    return True
            else:
                return True
        
        if len(indegree_zeros) > 1 or not indegree_zeros:
            return False
        
        ans = dfs(indegree_zeros.pop())

        for color in colors:
            if color == 0:
                return False
        return ans





