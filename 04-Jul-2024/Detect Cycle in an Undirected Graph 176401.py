# Problem: Detect Cycle in an Undirected Graph - https://practice.geeksforgeeks.org/problems/detect-cycle-in-an-undirected-graph/1

from typing import List
class Solution:
    #Function to detect cycle in an undirected graph.
	def isCycle(self, V: int, adj: List[List[int]]) -> bool:
	    visited = [0 for i in range(V)]

		def dfs(start):
            stack = [(start, -1)]  # Stack of (node, parent)
            while stack:
                node, parent = stack.pop()
                if visited[node]:
                    continue
                visited[node] = True
                for a in adj[node]:
                    if not visited[a]:
                        stack.append((a, node))
                    elif a != parent:
                        return True
            return False
		    
	    for i in range(V):
	        if visited[i] == 0:
	            if dfs(i):
	                return True
	    return False