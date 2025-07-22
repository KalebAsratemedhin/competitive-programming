# Last updated: 7/22/2025, 3:25:54 PM
class UnionFind:

    def __init__(self, n):
        self.root = list(range(n))
        self.rank = [1 for _ in range(n)]
        self.sum = collections.defaultdict(int)

    def add_and_merge(self, i: int, num: int) -> int:
        self.sum[i] = num
        if i - 1 in self.sum:
            self.union(i - 1, i)
        if i + 1 in self.sum:
            self.union(i, i + 1)
        root_i = self.find(i)
        return self.sum[root_i]

    def find(self, x: int) -> int:
        if self.root[x] != x: self.root[x] = self.find(self.root[x])
        return self.root[x]

    def union(self, x: int, y: int) -> None:
        root_x, root_y = self.find(x), self.find(y)
        if root_x == root_y: 
            return
        if self.rank[root_x] > self.rank[root_y]: 
            self.root[root_y] = root_x
            self.sum[root_x] += self.sum[root_y]
        elif self.rank[root_x] < self.rank[root_y]: 
            self.root[root_x] = root_y
            self.sum[root_y] += self.sum[root_x]
        else:
            self.root[root_y] = root_x
            self.rank[root_x] += 1
            self.sum[root_x] += self.sum[root_y]

    def is_connected(self, x: int, y: int) -> bool:
        return self.find(x) == self.find(y)


class Solution:
    def maximumSegmentSum(self, nums: List[int], removeQueries: List[int]) -> List[int]:
        n = len(nums)
        uf = UnionFind(n)
        ans = [0 for _ in range(n)]
        max_segment_sum = 0

        for i in range(n - 1, -1, -1):
            ans[i] = max_segment_sum
            query = removeQueries[i]
            max_segment_sum = max(max_segment_sum, uf.add_and_merge(query, nums[query]))
        return ans