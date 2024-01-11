class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        n = len(nums)
        i = j = 0
        dict = {}
        ans = 0
        sum = 0
        while j < n:
            if nums[j] in dict:
                del dict[nums[i]]
                sum -= nums[i]
                i += 1
            else:
                dict[nums[j]] = j 
                sum += nums[j]
                ans = max(ans, sum)
                j += 1
        return ans 

