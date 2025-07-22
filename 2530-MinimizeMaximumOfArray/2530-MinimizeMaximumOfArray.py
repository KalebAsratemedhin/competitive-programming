# Last updated: 7/22/2025, 3:25:34 PM
class Solution:
    def minimizeArrayValue(self, nums: List[int]) -> int:
        maxima, prefix = 0, 0

        for i in range(len(nums)):
            prefix += nums[i]
            maxima = max(maxima, (prefix + i) / (i + 1))

        return int(maxima)

