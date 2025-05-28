class Solution:
    def maxTargetNodes(self, edges1: List[List[int]], edges2: List[List[int]], k: int) -> List[int]:

        tree = defaultdict(list)

        for u, v in edges2:
            tree[u].append(v)
            tree[v].append(u)

        visited = set()


        def dfs(node, curr):
            if curr == 0:
                return 1

            if curr < 0:
                return 0
            
            visited.add(node)
            targets = 1
            for adj in tree[node]:
                if adj not in visited:
                    targets += dfs(adj, curr - 1)
            
            visited.remove(node)
            return targets

        max2 = 0
        for node in list(tree.keys()):
            temp = dfs(node, k - 1)
            print(temp, " ", node)
            max2 = max(max2, temp)


        print(max2)

        visited = set()
        tree = defaultdict(list)

        for u, v in edges1:
            tree[u].append(v)
            tree[v].append(u)
        
        ans = []
        for i in range(len(list(tree.keys()))):
            temp = dfs(i, k)
            print(f"{temp} and {i}")
            ans.append(temp + max2 )

        return ans
        
