# Problem: Build a Matrix With Conditions - https://leetcode.com/problems/build-a-matrix-with-conditions/

class Solution:
    def buildMatrix(self, k: int, rowConditions: List[List[int]], colConditions: List[List[int]]) -> List[List[int]]:
        def topSort(adjList):
            graph = [[] for i in range(k)]
            indegrees = [0 for i in range(k)]

            for u, v in adjList:
                graph[u - 1].append(v - 1)
                indegrees[v - 1] += 1
            
            queue = deque()
            for i in range(k):
                if indegrees[i] == 0:
                    queue.append(i)

            order = []
            while queue:
                node = queue.popleft()
                order.append(node + 1)
                for adj in graph[node]:
                    indegrees[adj] -= 1
                    if indegrees[adj] == 0:
                        queue.append(adj)
            
            return order

        rowOrder = topSort(rowConditions)
        colOrder = topSort(colConditions)

        if len(rowOrder) < k or len(colOrder) < k:
            return []

        matrix = [[0 for i in range(k)] for j in range(k)]

        for i in range(k):
            for j in range(k):
                if rowOrder[i] == colOrder[j]:
                    matrix[i][j] = rowOrder[i]
        return matrix

