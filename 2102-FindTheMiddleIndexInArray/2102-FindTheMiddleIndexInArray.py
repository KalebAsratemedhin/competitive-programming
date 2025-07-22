# Last updated: 7/22/2025, 3:27:29 PM
class Solution:
    def findMiddleIndex(self, nums: List[int]) -> int:
        n = len(nums)
        sum = 0
        left = 0
        for num in nums:
            sum += num
        for i in range(n):
            sum -= nums[i]
            if left == sum:
                return i
            left += nums[i]
        return -1