class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        n = len(nums)
        sum = 0
        ans = - 100000
        for num in nums:
            sum += num
            ans = max(ans, sum) 
            if sum < 0:
                sum = 0

        return ans
