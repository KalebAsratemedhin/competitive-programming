# Last updated: 7/22/2025, 3:24:49 PM
class Solution:
    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:
        # 0 1 2 4 4 5 7
        # 0 1 4 4 5 7 

        # 1 2 5 7 9

        n = len(nums)
        right = left = n - 1
        nums.sort()
        count = 0

        for i in range(n):
            if left < i:
                left = i
            
            if right < i:
                right = i
        
            while left > i and nums[left] + nums[i] >= lower:
                left -= 1
            while right > i and nums[right] + nums[i] > upper:
                right -= 1
                
            count += right - left 
        
        return count




