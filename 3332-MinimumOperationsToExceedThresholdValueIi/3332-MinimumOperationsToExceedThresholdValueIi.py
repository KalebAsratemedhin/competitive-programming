# Last updated: 7/22/2025, 3:23:33 PM
class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        heapq.heapify(nums)
        ops = 0

        while len(nums) >= 2 and nums[0] < k:
            x, y = heapq.heappop(nums), heapq.heappop(nums)
            heapq.heappush(nums, min(x, y) * 2 + max(x, y))
            ops += 1
    
        return ops



