# Problem: C. Restructuring Company - https://codeforces.com/edu/course/2/lesson/7/2/practice/contest/289391/problem/C

import sys, threading
input = lambda: sys.stdin.readline().strip()
class UnionFind:
    def __init__(self, size):
        self.root = [i for i in range(size + 1)]
        self.rank = [1 for _ in self.root]
        self.nexts = [i + 1 for i in range(size + 1)]
    
    def find(self, vertex):
        if vertex == self.root[vertex]:
            return vertex
        self.root[vertex] = self.find(self.root[vertex])
        return self.root[vertex]
    
    def union(self, v1, v2):
        root1 = self.find(v1)
        root2 = self.find(v2)
        
        if root1 != root2:
            if self.rank[root1] > self.rank[root2]:
                self.root[root2] = root1
            elif self.rank[root1] < self.rank[root2]:
                self.root[root1] = root2
            else:
                self.root[root2] = root1
                self.rank[root1] += 1

    def is_connected(self, x, y):
        return self.find(x) == self.find(y)
    
    def range_union(self, x, y):
        i = x
        while i <= y:
            self.union(x, i)
            temp = self.nexts[i]
            self.nexts[i] = self.nexts[y]  
            i = temp

def main():

    n, q = map(int, input().split())
    uf = UnionFind(n)

    for _ in range(q):
        type, x, y = map(int, input().split())

        if type == 1:
            uf.union(x, y)

        elif type == 2:
            uf.range_union(x, y)

        else:
            if uf.is_connected(x, y):
                print("YES")
            else:
                print("NO")

if __name__ == '__main__':
    sys.setrecursionlimit(1 << 30)
    threading.stack_size(1 << 27)
    main_thread = threading.Thread(target=main)
    main_thread.start()
    main_thread.join()