class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        prefix = []
        sum = 0
        for num in nums:
            sum += num
            prefix.append(sum)
        return prefix