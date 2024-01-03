class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort()
        n = len(piles)
        k = n // 3
        ans = 0
        for i in range(n - k):
            if i % 2 == 0:
                ans += piles[i + k]
        return ans


