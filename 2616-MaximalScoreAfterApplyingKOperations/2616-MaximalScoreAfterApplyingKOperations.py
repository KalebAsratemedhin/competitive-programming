# Last updated: 7/22/2025, 3:25:07 PM
class Solution:
    def maxKelements(self, nums: List[int], k: int) -> int:
        heap = []

        for num in nums:
            heapq.heappush(heap, -num)
        score = 0

        for i in range(k):
            num = -1 * heapq.heappop(heap)
            score += num
            heapq.heappush(heap, -1 * ceil(num / 3))

        return score



