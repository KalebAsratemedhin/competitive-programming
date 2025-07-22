# Last updated: 7/22/2025, 3:26:05 PM
class Solution:
    def closestMeetingNode(self, edges: List[int], node1: int, node2: int) -> int:
        dist1 = [-1 for i in range(len(edges))]
        dist2 = [-1 for i in range(len(edges))]

        def dfs(node, dist, curr):
            dist[node] = curr


            if edges[node] != -1 and node != edges[node] and dist[edges[node]] == -1:
                dfs(edges[node], dist, curr + 1)

        dfs(node1, dist1, 1)
        dfs(node2, dist2, 1)
        

        ans, ind = float("inf"), -1

        for i in range(len(edges)):
            if dist1[i] != -1 and dist2[i] != -1:
                if max(dist1[i], dist2[i]) < ans:
                    ans = max(dist1[i], dist2[i])
                    ind = i
        return ind
        
