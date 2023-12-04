class Solution:
    def decompressRLElist(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = []
        for i in range(0, n, +2):
            ans += nums[i] * [nums[i + 1]]
        return ans