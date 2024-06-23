# Problem: Find Pivot Index - https://leetcode.com/problems/find-pivot-index/

class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        total = sum([num for num in nums])
        left = 0
        for i in range(len(nums)):
            total -= nums[i]
            if left == total:
                return i
            left += nums[i]
        return -1