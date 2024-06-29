# Problem: All Ancestors of A Node in Directed Acyclic Graph - https://leetcode.com/problems/all-ancestors-of-a-node-in-a-directed-acyclic-graph/

class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        adjacents = [[] for i in range(n)]
        reverse_graph = [[] for i in range(n)]
        incoming = [0] * n

        for a, b in edges:
            adjacents[a].append(b)
            reverse_graph[b].append(a)
            incoming[b] += 1

        queue = deque()
        for i in range(n):
            if incoming[i] == 0:
                queue.append(i)

        topological_order = []
        while queue:
            node = queue.popleft()
            topological_order.append(node)
            for adj in adjacents[node]:
                incoming[adj] -= 1
                if incoming[adj] == 0:
                    queue.append(adj)

        predecessors = [ 0 for i in range(n)]
        for node in topological_order:
            parents = set(reverse_graph[node])
            for adj in reverse_graph[node]:
                parents = parents.union(predecessors[adj])

            predecessors[node] = sorted(list(parents))

        return predecessors


            

            
