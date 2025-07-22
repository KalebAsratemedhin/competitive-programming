# Last updated: 7/22/2025, 3:26:13 PM
class UnionFind:
    def __init__(self, size):
        self.root = [i for i in range(size)]
        self.rank = [0] * size
        
    
    def find(self, x):
        if x == self.root[x]:
            return x
        self.root[x] = self.find(self.root[x])
        return self.root[x]
      

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
    def is_connected(self, x, y):
        return self.find(x) == self.find(y)

class Solution:
    def countPairs(self, n: int, edges: List[List[int]]) -> int:
        uf = UnionFind(n)
        for u, v in edges:
            if not uf.is_connected(u, v):
                uf.union(u, v)
        
        reps = {}
        for node in range(n):
            reps[uf.find(node)] = reps.get(uf.find(node), 0) + 1
        
        total, count = n, 0
        for freq in reps.values():
            total -= freq
            count += freq * (total)
        return count



        
        