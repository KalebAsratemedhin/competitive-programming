# Last updated: 7/22/2025, 3:27:31 PM
class Solution:
    def minStoneSum(self, piles: List[int], k: int) -> int:
        heapq.heapify(piles)
        ans = 0

        while len(piles) > k:
            ans += heapq.heappop(piles)
        
        piles = [-1 * pile for pile in piles]
        heapq.heapify(piles)
        while k > 0 and piles:
            pile = -1 * heapq.heappop(piles)
            pile -= pile // 2
            heapq.heappush( piles, -1 * pile)
            k -= 1
        ans += sum([-1 * pile for pile in piles])
        return ans


