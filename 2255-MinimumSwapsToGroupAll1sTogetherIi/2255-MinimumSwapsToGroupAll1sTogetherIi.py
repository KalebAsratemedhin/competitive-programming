# Last updated: 7/22/2025, 3:26:47 PM
class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        count = nums.count(1)
        nums += nums
        temp = 0
        left = 0
        ans = count
        for right in range(len(nums)):
            if right - left + 1 <= count:
                if nums[right] == 0:
                    temp += 1
            
            if right - left + 1 == count:
                ans = min(ans, temp)
                if nums[left] == 0:
                    temp -= 1
                left += 1
            
            
        return ans

