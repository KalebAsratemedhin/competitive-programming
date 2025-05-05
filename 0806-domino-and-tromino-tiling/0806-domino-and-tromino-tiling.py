class Solution(object):
    def numTilings(self, n):
        mod = int(1e9 + 7)
        
        @cache
        def dominoes(i, possible):
            if i == n:
                return 0 if possible else 1
            if i > n:
                return 0
            if possible:
                return (dominoes(i + 1, False) + dominoes(i + 1, True)) % mod
            return (dominoes(i + 1, False) + dominoes(i + 2, False) + 2 * dominoes(i + 2, True)) % mod
        
        return dominoes(0, False)