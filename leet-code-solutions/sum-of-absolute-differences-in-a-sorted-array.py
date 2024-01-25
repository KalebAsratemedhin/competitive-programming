class Solution:
    def getSumAbsoluteDifferences(self, nums: List[int]) -> List[int]:
        n = len(nums)
        sum = 0
        ref = nums[0]
        result = []
        for i in range(1, n):
            sum += nums[i] - ref
        result.append(sum)
        for i in range(1, n):
            diff = nums[i] - ref
            ref = nums[i]
            sum += (-diff * (n - i) + i * diff)
            result.append(sum)
        return result