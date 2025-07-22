# Last updated: 7/22/2025, 3:25:08 PM
class Solution:
    def maximumCount(self, nums: List[int]) -> int:
        neg = pos = 0
        for i, num in enumerate(nums):
            if num < 0:
                neg += 1
            elif num > 0:
                pos += 1
                
        return max(neg, pos)