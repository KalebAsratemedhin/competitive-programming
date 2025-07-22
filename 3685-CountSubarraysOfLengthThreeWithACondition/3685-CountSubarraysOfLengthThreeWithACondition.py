# Last updated: 7/22/2025, 3:22:49 PM
class Solution:
    def countSubarrays(self, nums: List[int]) -> int:
        count = 0

        for i in range(2, len(nums)):
            if 2 * ( nums[i - 2] + nums[i]) == nums[i - 1]:
                count += 1
        return count
