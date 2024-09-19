# Problem: Smallest String With Swaps - https://leetcode.com/problems/smallest-string-with-swaps/

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
    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
        uf = UnionFind(len(s))
        for u, v in pairs:

            if uf.find(u) != uf.find(v):
                uf.union(u, v)
        
        parents = defaultdict(list)
        for i in range(len(s)):
            parents[uf.find(i)].append(i)


        ans = [""] * len(s)
        for key, value in parents.items():
            letters = [s[l] for l in value]
            value.sort()
            letters.sort()

            for i in range(len(letters)):
                ans[value[i]] = letters[i]
           
        return "".join(ans)