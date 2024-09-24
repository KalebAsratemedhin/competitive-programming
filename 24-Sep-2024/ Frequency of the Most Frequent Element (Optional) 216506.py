# Problem:  Frequency of the Most Frequent Element (Optional) - https://leetcode.com/problems/frequency-of-the-most-frequent-element/

class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        nums.sort()
        left = 0
        difference = 0
        ans = 1

        for i in range(1, len(nums)):
            difference += (nums[i] - nums[i - 1]) * (i - left)

            while difference > k:
                difference -= (nums[i] - nums[left])
                left += 1

            ans = max(ans, i - left + 1)

        return ans

