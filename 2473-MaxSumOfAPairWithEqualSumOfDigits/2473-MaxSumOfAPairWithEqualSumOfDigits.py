# Last updated: 7/22/2025, 3:25:50 PM
class Solution:
    def maximumSum(self, nums: List[int]) -> int:
        digits = {}
        ans = -1

        for num in nums:
            sum_ = 0
            for c in str(num):
                sum_ += int(c)
           
            if sum_ in digits:
                ans = max(ans, num + digits[sum_])
                digits[sum_] = max(digits[sum_], num)   
            else:
                digits[sum_] = num

        return ans