# Last updated: 7/22/2025, 3:24:44 PM
class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        sum = 0
        left = 0
        answer = []
        for num in nums:
            sum += num
        for i in range(len(nums)):
            sum -= nums[i]
            answer.append(abs(sum - left))
            left += nums[i]
        return answer