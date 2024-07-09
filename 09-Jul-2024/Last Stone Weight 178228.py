# Problem: Last Stone Weight - https://leetcode.com/problems/last-stone-weight/

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-1 * stone for stone in stones]
        heapq.heapify(stones)
        
        while len(stones) > 1:
            y = -1 * heapq.heappop(stones)
            x = -1 * heapq.heappop(stones)
            stone = y - x
            if stone: heapq.heappush(stones, -1 * stone)
        return -1 * stones[-1] if len(stones) else 0

            
