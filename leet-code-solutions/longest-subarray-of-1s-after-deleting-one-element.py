class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        max_subarray = 0
        count = 0
        ones = 0
        left = 0
        n = len(nums)
        for i in range(n):
            while count >= 1 and nums[i] != 1 and left < n:
                if nums[left] == 1:
                    ones -= 1
                else:
                    count -= 1
                left += 1
            if nums[i] != 1 and count < 1:
                count += 1
            elif nums[i] == 1:
                ones += 1
                max_subarray = max(max_subarray, ones)
        if max_subarray == n:
            return n - 1
        
        return max_subarray
                
                