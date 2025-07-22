# Last updated: 7/22/2025, 3:23:48 PM
class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        window = {}
        _max = 0
        left = 0
        
        for r in range(len(nums)):
            window[nums[r]] = window.get(nums[r], 0) + 1

            while window[nums[r]] > k:
                window[nums[left]] -= 1
                if not window[nums[left]]:
                    del window[nums[left]]
                left += 1
            _max = max(_max, r - left + 1)
        return _max