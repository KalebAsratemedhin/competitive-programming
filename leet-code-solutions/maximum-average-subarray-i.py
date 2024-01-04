class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        sum = 0
        for i in range(k):
            sum += nums[i]
        max_sum = sum
        for i in range(k, len(nums)):
            sum += nums[i]
            sum -= nums[i - k]
            max_sum = max(sum, max_sum)
        return max_sum / k