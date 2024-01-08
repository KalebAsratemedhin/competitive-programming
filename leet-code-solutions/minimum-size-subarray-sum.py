class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        count = 0
        n = len(nums)
        i, j = 0, 0
        l = n + 1
        while i < n:
            if count < target and j < n:
                count += nums[j]
                j += 1
            elif count >= target:
                l = min(l, j - i)
                count -= nums[i]
                i += 1
            elif j >= n:
                break
        if l == n + 1:
            return 0
        return l