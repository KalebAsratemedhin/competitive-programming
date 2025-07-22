# Last updated: 7/22/2025, 3:24:53 PM
class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        heap = [-gift for gift in gifts]

        heapq.heapify(heap)
        while heap and k > 0:
            gift = -heapq.heappop(heap)
            heapq.heappush(heap, -math.floor(math.sqrt(gift)))
            k -= 1
        return -sum(heap)