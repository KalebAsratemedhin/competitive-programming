# Last updated: 7/22/2025, 3:25:29 PM
class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        left = 0

        for i in range(len(nums) - 1):
            if nums[i] == nums[i + 1]:
                nums[i] *= 2
                nums[i + 1] = 0
        
        for right in range(len(nums)):
            while nums[left] and left < right:
                left += 1
                
            if nums[right] and not nums[left]:
                nums[right], nums[left] = nums[left], nums[right]
                left += 1

        return nums
