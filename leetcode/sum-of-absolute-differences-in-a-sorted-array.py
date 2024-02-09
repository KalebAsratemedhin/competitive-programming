class Solution:
    def getSumAbsoluteDifferences(self, nums: List[int]) -> List[int]:
        n = len(nums)
        sum = 0
        ref = nums[0]
        result = []
        suffix = [0] * n
        prefix = [0] * n

        sum = 0

        for i in range(n):
            sum += nums[i]
            prefix[i] = sum
        
        sum = 0
        for j in range(n - 1, -1, -1):
            sum += nums[j]
            suffix[j] = sum
        
        for i in range(n):
            res = 0
            if i > 0:
                res += nums[i] * i - prefix[i - 1]
            if i < n - 1:
                res += suffix[i + 1] - (n - i - 1) * nums[i]
            result.append(res)


        
        return result