class Solution:
    def reductionOperations(self, nums: List[int]) -> int:
        operations = 0
        nums.sort()
        n = len(nums) 
        for j in range(n - 1):
            if nums[j] < nums[j + 1]:
                operations += n - 1 - j
        return operations
