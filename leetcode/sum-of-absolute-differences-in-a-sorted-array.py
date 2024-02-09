class Solution:
    def getSumAbsoluteDifferences(self, nums: List[int]) -> List[int]:
        n = len(nums)
        result = []
        prefix = [0] * n
        sum = 0

        for i in range(n):
            sum += nums[i]
            prefix[i] = sum
        
        for i in range(n):
            res = 0
            if i > 0:
                res += nums[i] * i - prefix[i - 1]
            if i < n - 1:
                res += prefix[-1] - prefix[i] - (n - i - 1) * nums[i]
            result.append(res)

        return result