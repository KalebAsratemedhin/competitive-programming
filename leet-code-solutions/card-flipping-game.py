class Solution:
    def flipgame(self, fronts: List[int], backs: List[int]) -> int:
        n =  len(fronts)
        diff = set(fronts).union(set(backs))
        for i in range(n):
            if fronts[i] == backs[i]:
                diff.discard(fronts[i])
        if len(diff) == 0:
            return 0
        return min(list(diff))

        


