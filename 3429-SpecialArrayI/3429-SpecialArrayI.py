# Last updated: 7/22/2025, 3:23:21 PM
class Solution:
    def isArraySpecial(self, nums: List[int]) -> bool:
        
        for i in range(1, len(nums)):
            if not (nums[i - 1] + nums[i]) % 2:
                return False
        
        return True