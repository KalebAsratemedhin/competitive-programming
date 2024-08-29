# Problem: Most Stones Removed with Same Row or Column - https://leetcode.com/problems/most-stones-removed-with-same-row-or-column/

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
    def removeStones(self, stones: List[List[int]]) -> int:
        n = len(stones)
        connected = n
        uf = UnionFind(n)
        
        for i in range(n):
            stones[i].append(i)
            
        stones.sort()
        for i in range(n - 1):
            if stones[i][0] == stones[i + 1][0]:
                if uf.find(stones[i][2]) != uf.find(stones[i + 1][2]):
                    uf.union(stones[i][2], stones[i + 1][2])
                    connected -= 1
        
        stones.sort(key = lambda x: x[1])
        for i in range(n - 1):
            if stones[i][1] == stones[i + 1][1]:
                if uf.find(stones[i][2]) != uf.find(stones[i + 1][2]):
                    uf.union(stones[i][2], stones[i + 1][2])
                    connected -= 1


        return n - connected
        

