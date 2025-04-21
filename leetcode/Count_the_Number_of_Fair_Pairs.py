class Solution:
    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> 
int:
        n = len(nums)
        right = left = n - 1
        nums.sort()
        count = 0
        for i in range(n):
            if left < i:
                left = i
            
            if right < i:
                right = i
        
            while left > i and nums[left] + nums[i] >= lower:
                left -= 1
            while right > i and nums[right] + nums[i] > upper:
                right -= 1