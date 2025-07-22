# Last updated: 7/22/2025, 3:23:07 PM
class Solution:
    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:
        heap = [[num, i] for i, num in enumerate(nums)]
        heapq.heapify(heap)


        for i in range(k):
            min_, ind = heapq.heappop(heap)
            nums[ind] *= multiplier
            heapq.heappush(heap, [nums[ind], ind])
        return nums