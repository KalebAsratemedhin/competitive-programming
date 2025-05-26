class Solution(object):
    def largestPathValue(self, colors, edges):
        inf = float('inf')
        n = len(colors)
        adj = defaultdict(list)

        for u, v in edges:
            adj[u].append(v)
        
        count = [[0]*26 for _ in range(n)]
        visited = [0]*n
        
        def dfs(node):
            if visited[node] == 1:
                return inf   
            if visited[node] == 2:
                return count[node][ord(colors[node]) - ord('a')]
            
            visited[node] = 1
            for nxt in adj[node]:
                res = dfs(nxt)
                if res == inf:
                    return inf
                for c in range(26):
                    count[node][c] = max(count[node][c], count[nxt][c])
            
            col = ord(colors[node]) - ord('a')
            count[node][col] += 1
            visited[node] = 2  
            
            return count[node][col]
        
        ans = 0
        for i in range(n):
            val = dfs(i)
            if val == inf:
                return -1
            ans = max(ans, val)
        
        return ans