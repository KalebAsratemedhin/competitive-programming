# Last updated: 7/22/2025, 3:25:14 PM
class Solution:
    def longestSquareStreak(self, nums: List[int]) -> int:
        nums_set = set(nums)
        max_length = 0

        for num in nums:
            root = sqrt(num)

            if root in nums_set:
                continue
            
            curr = num
            i = 0
            while curr in nums_set:
                curr *= curr
                i += 1

            max_length = max(max_length, i)
            
        return -1 if max_length == 1 else max_length

