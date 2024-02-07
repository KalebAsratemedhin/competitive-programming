class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        sum = 0
        count = 0
        n = len(nums)
        prefix = {0:1}

        for i in range(n):
            sum += nums[i]
            count += prefix.get(sum - goal, 0)
            prefix[sum] = prefix.get(sum, 0) + 1
        return count


