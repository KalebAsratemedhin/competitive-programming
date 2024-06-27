# Problem: Find Center of Star Graph - https://leetcode.com/problems/find-center-of-star-graph/

class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        adjacents = [set() for i in range(len(edges) + 1)]

        for u, v in edges:
           adjacents[u - 1].add(v)
           adjacents[v - 1].add(u)


        for index, adjs in enumerate(adjacents):
            if len(adjs) > 1:
                return index + 1
            