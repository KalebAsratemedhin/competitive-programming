# Last updated: 7/22/2025, 3:23:26 PM
class Solution:
    def minimumSubarrayLength(self, nums: List[int], k: int) -> int:
        # have two pointers left and right
        # move right as long as bitwise or is less than k
        # move left while or is greater or equal to k and left doesn't exceed right
        # keep min of length

        
        ans = float('inf')
        left = 0
        window = [0] * 32

        def is_window_greater():
            for i in range(31, -1, -1):
                curr = k & (1 << i)
                if not curr and window[i] > 0:
                    return True
                if curr and window[i] <= 0:
                    return False
            return True



        for right in range(len(nums)):
            for i in range(32):
                if nums[right] & (1 << i):
                    window[i] += 1
                    
            while left <= right and is_window_greater():
                ans = min(ans, right - left + 1)
                for i in range(32):
                    if nums[left] & (1 << i):
                        window[i] -= 1
                left += 1
                
        if ans == float('inf'):
            return -1
        return ans
            
                    

            

