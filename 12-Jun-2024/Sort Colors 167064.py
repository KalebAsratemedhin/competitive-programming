# Problem: Sort Colors - https://leetcode.com/problems/sort-colors/

class Solution(object):
    def sortColors(self, nums):
        count = Counter(nums)
        index = 0
        for color in [0, 1, 2]:
            for j in range(count[color]):
                nums[index + j] = color
            index += count[color]
        
        