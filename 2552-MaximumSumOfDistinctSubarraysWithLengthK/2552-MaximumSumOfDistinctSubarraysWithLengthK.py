# Last updated: 7/22/2025, 3:25:28 PM
class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        left = 0
        window = {}
        window_sum = 0
        ans = 0

        for i in range(k):
            window[nums[i]] = window.get(nums[i], 0) + 1
            window_sum += nums[i]

        if len(window) == k:
            ans = max(window_sum, ans)

        for right in range(k, len(nums)):
            window[nums[right]] = window.get(nums[right], 0) + 1
            window_sum -= nums[left]
            window_sum += nums[right]
            window[nums[left]] -= 1
            if not window[nums[left]]:
                del window[nums[left]]

            left += 1

            if len(window) == k:
                ans = max(window_sum, ans)
        return ans
            
        


