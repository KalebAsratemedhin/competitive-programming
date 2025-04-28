class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        window = 0
        left = count = 0


        for right in range(len(nums)):
            window += nums[right]

            while left < right and window * (right - left + 1) >= k:
                window -= nums[left]
                left += 1

            if window * (right - left + 1) < k:
                count += right - left + 1
        
        return count

            

