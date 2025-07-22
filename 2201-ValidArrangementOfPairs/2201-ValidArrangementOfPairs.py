# Last updated: 7/22/2025, 3:27:00 PM
class Solution:
    def validArrangement(self, pairs: List[List[int]]) -> List[List[int]]:
        graph = defaultdict(list)
        indegrees = defaultdict(int)

        for u, v in pairs:
            graph[u].append(v)
            indegrees[v] += 1

        
        start = pairs[0][0]

        for key, val in graph.items():
            if len(val) > indegrees[key]:
                start = key
                break

        path = []
        def dfs(node):
            while graph[node]:
                adj = graph[node].pop()
                dfs(adj)
                path.append((node, adj))
        

        dfs(start)
        return path[::-1]

