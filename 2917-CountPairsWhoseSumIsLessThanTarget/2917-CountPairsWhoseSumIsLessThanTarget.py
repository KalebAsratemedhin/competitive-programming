# Last updated: 7/22/2025, 3:24:12 PM
class Solution:
    def countPairs(self, nums: List[int], target: int) -> int:
        nums.sort()
        left = 0
        right = len(nums) - 1
        count = 0
        for left in range(len(nums)):
            while left < right:
                if nums[left] + nums[right] < target:
                    count += (right - left)
                    break
                
                right -= 1

        return count


