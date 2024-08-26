# Problem: Minimum Number of Vertices to Reach All Nodes - https://leetcode.com/problems/minimum-number-of-vertices-to-reach-all-nodes/

class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        indegrees = [0] * n

        for u, v in edges:
            indegrees[v] = 1
            
        arr = []
        for i, node in enumerate(indegrees):
            if not node:
                arr.append(i)

        return arr