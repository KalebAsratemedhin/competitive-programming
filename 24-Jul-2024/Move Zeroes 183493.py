# Problem: Move Zeroes - https://leetcode.com/problems/move-zeroes/

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        place = 0

        for i in range(len(nums)):
            if nums[i] != 0:
                nums[place], nums[i] = nums[i], nums[place]
                place += 1
        

