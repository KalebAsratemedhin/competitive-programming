class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        zero, one = nums.count(0), nums.count(1)

        for i in range(len(nums)):
            if i < zero:
                nums[i] = 0
            elif i < zero + one:
                nums[i] = 1
            elif i < len(nums):
                nums[i] = 2
        
        