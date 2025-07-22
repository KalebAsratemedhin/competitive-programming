# Last updated: 7/22/2025, 3:25:45 PM
class Solution:
    def findSubarrays(self, nums: List[int]) -> bool:
        sums = {}
        for i in range(len(nums) - 1):
            sum = nums[i] + nums[i + 1]
            if sum in sums:
                return True
            sums[sum] = sums.get(sum, 0) + 1

        return False