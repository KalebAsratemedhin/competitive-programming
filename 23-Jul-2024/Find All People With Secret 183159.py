# Problem: Find All People With Secret - https://leetcode.com/problems/find-all-people-with-secret/

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

    def reset(self, x):
        self.root[x] = x
        self.rank[x] = 1

class Solution:
    def findAllPeople(self, n: int, meetings: List[List[int]], firstPerson: int) -> List[int]:
        uf = UnionFind(n)
        meetings.sort(key = lambda x: x[2])

        uf.union(0, firstPerson)
        meeting_time = defaultdict(list)

        for x, y, time in meetings:
            meeting_time[time].append((x, y))

        for key, value in meeting_time.items():
            for x, y in value:
                if not uf.is_connected(x, y):
                    uf.union(x, y)
                
            for x, y in value:
                if not uf.is_connected(x, 0):
                    uf.reset(x)
                    uf.reset(y)

        return [node for node in range(n) if uf.is_connected(0, node)]
