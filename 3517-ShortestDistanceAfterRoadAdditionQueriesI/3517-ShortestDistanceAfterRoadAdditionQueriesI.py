# Last updated: 7/22/2025, 3:23:12 PM
class Solution:
    def shortestDistanceAfterQueries(self, n: int, queries: List[List[int]]) -> List[int]:

        graph = [[i + 1] for i in range(n - 1)]
        ans = []

        def bfs(graph):
            queue = deque([0])
            level = 0
            visited = [0] * (n)
            visited[0] = 1

            while queue:
                for i in range(len(queue)):
                    node = queue.popleft()
                    if node == n - 1:
                        return level

                    for adj in graph[node]:
                        if not visited[adj]:
                            visited[adj] = 1
                            queue.append(adj)
                level += 1
                
                

        for u, v in queries:
            graph[u].append(v)
            ans.append(bfs(graph))
            

        return ans


