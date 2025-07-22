# Last updated: 7/22/2025, 3:25:39 PM
class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        i = max_and = max_len = 0
        n = len(nums)
        
        while i < n:
            prev = nums[i]
            count = 0
            while i < n and prev & nums[i] == max(prev, nums[i]):
                i += 1
                count += 1

            if prev == max_and and count > max_len:
                max_len = count
                max_and = prev
            elif prev > max_and:
                max_len = count
                max_and = prev
 
        return max_len



