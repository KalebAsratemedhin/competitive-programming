class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:
        def helper(l, r, nums):
            if r == l:
                return nums[l]
            first = nums[l] - helper(l + 1, r, nums) 
            last = nums[r] - helper(l, r - 1, nums) 
            return max(first, last)
            
        return helper(0, len(nums) - 1, nums) >= 0
 
      