class Solution:
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
        count = 0
        pairs = defaultdict(int)

        for i in range(len(dominoes)):
            pairs[tuple(sorted(dominoes[i]))] += 1

        for key, val in pairs.items():
            count += val * (val - 1) // 2
        return count