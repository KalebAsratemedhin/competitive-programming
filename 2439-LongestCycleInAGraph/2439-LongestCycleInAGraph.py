# Last updated: 7/22/2025, 3:26:04 PM
class Solution:
    def longestCycle(self, edges: List[int]) -> int:
        visited = [0] * len(edges)

        def dfs(node, dist):
            visited[node] = (1, dist)
            if edges[node] != -1:
                
                if visited[edges[node]] == 0:
                    temp = dfs(edges[node], dist + 1)
                    visited[node] = (2, dist)
                    return temp

                elif visited[edges[node]][0] == 1:
                    visited[node] = (2, dist)
                    return dist - visited[edges[node]][1] + 1
            
                    
            visited[node] = (2, dist)
            return -1

        ans = -1
        for i in range(len(edges)):
            if visited[i] == 0:
                ans = max(ans, dfs(i,0))


        return ans


'''
0 -> 3 -> 2 <- 5
|<--------|
1 -> 4
2 - 0
3 - 2
4 
5 - 2

[3, 4, 0, 2, -1, 2]
'''