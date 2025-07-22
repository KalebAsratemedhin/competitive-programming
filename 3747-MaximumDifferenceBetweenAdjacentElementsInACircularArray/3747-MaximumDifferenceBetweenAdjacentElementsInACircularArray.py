# Last updated: 7/22/2025, 3:22:47 PM
class Solution:
    def maxAdjacentDistance(self, nums: List[int]) -> int:
        ans = abs(nums[-1] - nums[0])

        for i in range(len(nums) - 1):
            ans = max(ans, abs(nums[i + 1] - nums[i]))
        return ans
            