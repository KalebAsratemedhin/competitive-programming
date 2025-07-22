# Last updated: 7/22/2025, 3:27:24 PM
class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        adj_list = [[] for i in range(n)]
        for edge in edges:
            adj_list[edge[0]].append(edge[1])
            adj_list[edge[1]].append(edge[0])

        def dfs(node, visited):
            visited.add(node)
            if node == destination:
                return True
            
            for neighbour in adj_list[node]:
                if neighbour not in visited:
                    if dfs(neighbour, visited):
                        return True
            return False
        
        visited = set()
        return dfs(source, visited)



