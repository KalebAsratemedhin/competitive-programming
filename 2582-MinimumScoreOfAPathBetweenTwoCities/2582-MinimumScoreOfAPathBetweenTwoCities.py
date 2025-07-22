# Last updated: 7/22/2025, 3:25:15 PM
class UnionFind:
    def __init__(self, size):
        self.root = [i for i in range(size)]
        self.rank = [0] * size
    
    def find(self, x):
        node = x
        while node != self.root[node]:
            node = self.root[node]

        while x != self.root[x]:
            temp = self.root[x]
            self.root[x] = node
            x = temp
        return x

    def union(self, x, y):
        root_x = self.root[x]
        root_y = self.root[y]

        if root_x != root_y:
            if self.rank[root_x] < self.rank[root_y]:
                self.root[root_x] = root_y
            elif self.rank[root_x] > self.rank[root_y]:
                self.root[root_y] = root_x
            else:
                self.root[root_x] = root_y
                self.rank[root_y] += 1

        
class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        uf = UnionFind(n + 1)
        for a, b, distance in roads:
            if uf.find(a) != uf.find(b):
                uf.union(a, b)
        
        roads.sort(key = lambda x: x[2])
        for a, b, distance in roads:
            if uf.find(1) == uf.find(a):
                return distance
        