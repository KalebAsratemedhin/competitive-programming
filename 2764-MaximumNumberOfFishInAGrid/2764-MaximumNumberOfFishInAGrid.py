# Last updated: 7/22/2025, 3:24:35 PM
class UnionFind:
    def __init__(self, size, fishes):
        self.root = [i for i in range(size)]
        self.rank = [0] * size
        self.fishes = fishes
    
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
                self.fishes[root_y] += self.fishes[root_x]
            elif self.rank[root_x] > self.rank[root_y]:
                self.root[root_y] = root_x
                self.fishes[root_x] += self.fishes[root_y]
            else:
                self.root[root_x] = root_y
                self.fishes[root_y] += self.fishes[root_x]
                self.rank[root_y] += 1
    def is_connected(self, x, y):
        return self.find(x) == self.find(y)

class Solution:
    def findMaxFish(self, grid: List[List[int]]) -> int:
        n, m = len(grid[0]), len(grid)
        fishes = [0] * (n * m)
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] != 0:
                    fishes[i * n + j] += grid[i][j]

        def is_valid(r, c):
            return 0 <= r < m and 0 <= c < n and grid[r][c] != 0

        uf = UnionFind(n * m, fishes)
        directions = [(0, 1), (1, 0), (-1, 0), (0, -1)]
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:
                    continue
                for dx, dy in directions:
                    r, c = i + dx, j + dy
                    x = r * n + c
                    a = i * n + j
                    if is_valid(r, c) and not uf.is_connected(x, a):
                        uf.union(x, a)

        return max(uf.fishes)


        

        