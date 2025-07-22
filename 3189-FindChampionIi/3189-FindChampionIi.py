# Last updated: 7/22/2025, 3:23:56 PM
class Solution:
    def findChampion(self, n: int, edges: List[List[int]]) -> int:
        indegrees = {i: 0 for i in range(n)}

        for a, b in edges:
            indegrees[b] += 1
        
        ans = -1
        
        for key, val in indegrees.items():
            if not val and ans != -1:
                return -1

            if not val:
                ans = key

        return 0 if ans == -1 else ans



        