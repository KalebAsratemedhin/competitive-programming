# Last updated: 7/22/2025, 3:23:37 PM
class Solution:
    def returnToBoundaryCount(self, nums: List[int]) -> int:
        count = 0
        prefix = 0
        n = len(nums)

        for i in range(n):
            prefix += nums[i]
            if prefix == 0:
                count += 1
        return count