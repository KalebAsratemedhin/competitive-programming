# Problem: First Missing Positive - https://leetcode.com/problems/first-missing-positive/description/

class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            while nums[i] != i + 1 and 1 <= nums[i] <= len(nums):
                ind = nums[i] - 1
                if nums[i] == nums[ind]:
                    break

                nums[i], nums[ind] = nums[ind], nums[i]

        for i, num in enumerate(nums):
            if i + 1 != num:
                return i + 1
        return len(nums) + 1

