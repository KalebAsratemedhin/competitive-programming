# Last updated: 7/22/2025, 3:26:00 PM
class Solution:
    def minimumReplacement(self, nums: List[int]) -> int:
        operations = 0
        base = nums[-1]
        n = len(nums)
        for i in range(n - 2, -1, -1):
            if nums[i] % base == 0:
                spaces = nums[i] // base
            else:
                spaces = nums[i] // base + 1
            base = nums[i] // spaces
            operations += spaces - 1
        return operations




