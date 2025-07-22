# Last updated: 7/22/2025, 3:27:25 PM
class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        nums.sort()
        n = len(nums)
        i = j = 0
        ans = nums[n - 1] - nums[0]
        while i < n and j < n:
            if j - i + 1 < k:
                j += 1
            elif j - i + 1 == k:
                ans = min(ans, nums[j] - nums[i])
                j += 1
                i += 1
        return ans
