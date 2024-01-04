class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        operation = 0
        nums.sort()
        left = 0
        right = len(nums) - 1
        while left < right:
            if nums[right] > k - nums[left]:
                right -= 1
            elif nums[right] == k - nums[left]:
                operation += 1
                left += 1
                right -= 1
            else:
                left += 1
        return operation